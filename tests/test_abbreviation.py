from unittest import TestCase

from dynamic_programming.abbreviation import abbreviation, remove_lower_case_letter, find_first_matching_char, \
    conversion


class Test(TestCase):
    def test_conversion(self):

        input_data = "QOTLYiFECLAGIEWRQMWPSMWIOQSEBEOAuhuvo"
        convert_to = "QOTLYFECLAGIEWRQMWPSMWIOQSEBEOA"
        possible = conversion(input_data, convert_to)
        self.assertEqual("YES", possible)

        input_data = "beFgH"
        convert_to = "EFH"
        possible = conversion(input_data, convert_to)
        self.assertEqual("YES", possible)

        input_data = "EYONDOCHNZYYlBZXPGzX"
        convert_to = "EYONDOCHNZYYBZXPGXOG"
        possible = conversion(input_data, convert_to)
        self.assertEqual("NO", possible)


    def test_conversion_sample1(self):

        input_data = "daBcd"
        convert_to = "ABC"
        possible = conversion(input_data, convert_to)
        self.assertEqual(True, possible)

    def test_conversion_sample2(self):
        input_data = "hHhAhhcahhacaccacccahhchhcHcahaahhchhhchaachcaCchhchcaccccchhhcaahhhhcaacchccCaahhaahachhacaahhaachhhaaaCalhhchaccaAahHcchcazhachhhaaahaahhaacchAahccacahahhcHhccahaachAchahacaahcahacaahcahacaHhccccaahaahacaachcchhahhacchahhhaahcacacachhahchcaAhhcaahchHhhaacHcacahaccccaaahacCHhChchhhahhchcahaaCccccahhcaachhhacaaahcaaaccccaacaaHachaahcchaahhchhhcahahahhcaachhchacahhahahahAahaAcchahaahcaaaaahhChacahcacachacahcchHcaahchhcahaachnachhhhcachchahhhacHhCcaHhhhcaCccccaaahcahacahchahcaachcchaachahhhhhhhhcahhacacCcchahccaaaaaHhhccaAaaaCchahhccaahhacaccchhcahhcahaahhgacahcahhchcaaAccchahhhaahhccaaHcchaccacahHahChachhcaaacAhacacaacacchhchchacchchcacchachacaahachccchhhaccahcacchaccaahaaaccccccaaaaaaaHhcahcchmcHchcchaaahaccchaaachchHahcaccaaccahcacacahAhaacaacaccaccaaacahhhcacAhaCchcaacCcccachhchchcchhchahchchahchchhchcacaachahhccacachaAhaaachchhchchchhaachahaahahachhaaaccacahhcacchhhaaachaaacAahhcachchachhhcacchacaaChCahhhccahChaachhcahacchanaaacchhhccacacchcahccchAcahacaaachhacchachccaaHacaacAhahcCh"
        convert_to = "HAHHCHAACCCAHCHHAHHAHCACCHCCHHCAAHHCACCCAHHHACAAHHHHCHHCAHHAHHAAAHAACAAHAHHCAHAHACHACHCHACACHAAHHAAAHCAHHACACAACHHHCHAHCAHCHHHAHAHACCAAAHCHHCHHCCAACCCCAACHACAACAAHACHCHAHHACCHCAHHHAAACHACAACHCACACAHHCCHAHACCCACCAACHCHHHCCCCCHCCAHHCAAHHAHHHHHHHAACCCCAHCCAAAAAHHHAAAACCAHHCAHACACCHHCHAHAHHCHAACHHHHHCCHCCAHAHCHCAAACCACCCCHACCACHHACHHACACHACCAACCCCAAAAHHAHCHHHCCAHCCHACHHAHCCACACCHAHAAACACCCCAHCCAHACCCCCCHCCHHCHHHHCHCHCAHHHACHAHAACCCAAAACHAACAAAHHAAHAAAHACHHCACHCCHCHAACHACACHHCCCCCAHCACHAAAHCHCAHACAAC"
        self.assertTrue(abbreviation(input_data, convert_to))



    def test_remove_lower_case(self):
        input_data = "daBcd"
        expected = "B"
        self.assertEqual(remove_lower_case_letter(input_data), expected)
        input_data = ""
        expected = ""

        letter = remove_lower_case_letter(input_data)
        self.assertEqual(letter, expected)

    def test_find_first_matching_char(self):
        input_data = "DaBcd"
        match_against = "fAbcd"
        self.assertTrue(find_first_matching_char(input_data, match_against), (1, 1))
        input_data = "DaBcd"
        match_against = "f"
        self.assertTrue(find_first_matching_char(input_data, match_against), (-1, 1))