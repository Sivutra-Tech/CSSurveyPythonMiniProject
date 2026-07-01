import io
import os
import sys
import csv
import tempfile
import types
import unittest
from unittest.mock import patch

import movieData
import seatData
import ticket
import bookAMovie
import checkBooking
import menu


def debug_print(*args, **kwargs):
    print(*args, **kwargs)


class ProgramTestCase(unittest.TestCase):
    def test_movie_data_get_genre(self):
        genres = movieData.getGenre()
        self.assertIn("Horror", genres)
        self.assertIn("Sci_Fi", genres)

    def test_movie_data_get_movie(self):
        movies = movieData.getMovie("Horror")
        self.assertTrue(len(movies) >= 1)
        self.assertEqual(movies[0][2], "The Conjuring")

    def test_seat_data_book_and_get_seat(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpfile = os.path.join(tmpdir, "seat.csv")
            seatData.fileLocation = tmpfile
            seatData.setFreshSeat()

            seatData.bookSeat("A", 1)
            seats = seatData.getSeat()

            self.assertEqual(seats[0][0], "X")
            self.assertEqual(seats[0][1], "2")
            debug_print("Booked seat row A and seat number 1 -> first row:", seats[0], file=sys.__stdout__)

    def test_ticket_storage_write_and_search(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpfile = os.path.join(tmpdir, "ticketStorage.csv")
            ticket.fileLocation = tmpfile

            saved_ticket = ["TID-1", "Movie Name", "13:50", "23-June-2026", "A", "1"]
            ticket.addTicketToStorage(saved_ticket)
            result = ticket.searchTicket("TID-1")

            self.assertIsNotNone(result)
            self.assertEqual(result[0][1], "Movie Name")
            self.assertIsNone(ticket.searchTicket("MISSING-ID"))
            debug_print("Saved ticket:", saved_ticket, file=sys.__stdout__)
            debug_print("Search returned:", result[0], file=sys.__stdout__)

    def test_bookamovie_confirmation_list_state(self):
        initial_list = ["Movie Name", "13:50"]
        bookAMovie.setComfirmationList(initial_list, action="new")
        self.assertEqual(bookAMovie.getComfirmationList(), initial_list)
        debug_print("Initial confirmation list:", bookAMovie.getComfirmationList(), file=sys.__stdout__)

        updated_list = ["Updated Movie", "14:30"]
        bookAMovie.setComfirmationList(updated_list, action="update")
        self.assertEqual(bookAMovie.getComfirmationList(), updated_list)
        debug_print("Updated confirmation list:", bookAMovie.getComfirmationList(), file=sys.__stdout__)

    def test_checkbooking_found_prints_booking_details(self):
        with patch("builtins.input", return_value="TID-1"), \
                patch.object(checkBooking.ticket, "searchTicket", return_value=[["TID-1", "Movie Name", "13:50", "23-June-2026", "A", "1"]]), \
                patch("sys.stdout", new_callable=io.StringIO) as mocked_stdout:
            checkBooking.runCheckBooking()
            output = mocked_stdout.getvalue()
            self.assertIn("You book Movie Name at 13:50 on 23-June-2026 with seat row A and seat number 1", output)

    def test_checkbooking_not_found_prints_error(self):
        with patch("builtins.input", return_value="TID-99"), \
                patch.object(checkBooking.ticket, "searchTicket", return_value=None), \
                patch("sys.stdout", new_callable=io.StringIO) as mocked_stdout:
            checkBooking.runCheckBooking()
            self.assertIn("Ticket Not Found", mocked_stdout.getvalue())

    def test_menu_choice_check_booking(self):
        with patch("builtins.input", return_value="2"), \
                patch.object(checkBooking, "runCheckBooking") as mock_check, \
                patch("sys.stdout", new_callable=io.StringIO):
            menu.runMenu()
            mock_check.assert_called_once()

    def test_menu_choice_book_a_movie_uses_ticketpayment_stub(self):
        with patch("builtins.input", return_value="1"), \
                patch.object(bookAMovie, "runBookAMovie") as mock_book, \
                patch("sys.stdout", new_callable=io.StringIO):
            dummy_payment = types.ModuleType("ticketpayment")
            sys.modules["ticketpayment"] = dummy_payment
            try:
                menu.runMenu()
            finally:
                del sys.modules["ticketpayment"]
            mock_book.assert_called_once()

    def test_runprogram_import_calls_menu(self):
        import importlib

        dummy_menu = types.SimpleNamespace(runMenu=unittest.mock.MagicMock())
        sys.modules["menu"] = dummy_menu
        if "runProgram" in sys.modules:
            del sys.modules["runProgram"]

        try:
            import runProgram
            importlib.reload(runProgram)
            self.assertTrue(dummy_menu.runMenu.called)
        finally:
            sys.modules.pop("menu", None)
            sys.modules.pop("runProgram", None)


if __name__ == "__main__":
    unittest.main()
