from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Investice, Transakce, Poznamka

class InvesticeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.investice = Investice.objects.create(nazev="Testovací investice", popis="Popis testovací investice")

    def test_investice_creation(self):
        self.assertEqual(self.investice.nazev, "Testovací investice")
        self.assertEqual(self.investice.popis, "Popis testovací investice")

class TransakceModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.investice = Investice.objects.create(nazev="Testovací investice", popis="Popis testovací investice")
        self.transakce = Transakce.objects.create(investice=self.investice, datum="2025-05-10", cena=100, mnozstvi=10)

    def test_transakce_creation(self):
        self.assertEqual(self.transakce.cena, 100)
        self.assertEqual(self.transakce.mnozstvi, 10)

class PoznamkaModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.investice = Investice.objects.create(nazev="Testovací investice", popis="Popis testovací investice")
        self.poznamka = Poznamka.objects.create(investice=self.investice, obsah="Testovací poznámka")

    def test_poznamka_creation(self):
        self.assertEqual(self.poznamka.obsah, "Testovací poznámka")

class InvesticeViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.investice = Investice.objects.create(nazev="Testovací investice", popis="Popis testovací investice")

    def test_investice_list_view(self):
        response = self.client.get(reverse('investice_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Testovací investice")

    def test_investice_detail_view(self):
        response = self.client.get(reverse('investice_detail', kwargs={'pk': self.investice.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Popis testovací investice")

    def test_investice_create_view(self):
        response = self.client.post(reverse('add_investice'), {
            'nazev': "Nová investice",
            'typ': "akcie",
            'mena': "CZK",
            'popis': "Popis nové investice"
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Investice.objects.filter(nazev="Nová investice").exists())

    def test_investice_update_view(self):
        response = self.client.post(reverse('edit_investice', args=[self.investice.id]), {
            'nazev': "Upravená investice",
            'popis': "Upravený popis",
            'typ': "akcie",
            'mena': "CZK"
        })
        self.assertEqual(response.status_code, 302)
        self.investice.refresh_from_db()
        self.assertEqual(self.investice.nazev, "Upravená investice")

    def test_investice_delete_view(self):
        response = self.client.post(reverse('delete_investice', args=[self.investice.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Investice.objects.filter(id=self.investice.id).exists())
