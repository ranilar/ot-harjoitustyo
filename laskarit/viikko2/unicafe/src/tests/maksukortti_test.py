import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
        
    def test_saldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_rahan_lisays_toimii(self):
        self.maksukortti.lataa_rahaa(200)
        self.assertEqual(self.maksukortti.saldo_euroina(), 12.0)
        
    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(self.maksukortti.saldo_euroina(), 8.0)
    
    def test_liikaa_ottaessa_saldo_ei_muutu(self):
        self.maksukortti.ota_rahaa(1200)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
        
    def test_ota_rahaa_palauttaa_bool_oikein(self):
        self.assertEqual(self.maksukortti.ota_rahaa(200), True)
        self.assertEqual(self.maksukortti.ota_rahaa(1200), False)
        
    def test_konstruktori_asettaa_saldon_oikein(self):
        kortti = Maksukortti(1000)
        vastaus = str(kortti)

        self.assertEqual(vastaus, "Kortilla on rahaa 10.00 euroa")

