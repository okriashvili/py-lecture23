import main, unittest

# ფუნქცია / მეთოდების ტესტინგი################################################################################################
class TestClass(unittest.TestCase):
    # პირველრიგში ფუნქციის დასახელება აუცილებლად უნდა იწყებოდეს test დასახელებით
    # წინაააღმდეგ შემთხვევაში, ვერ წაიკითხავს და შედეგს არ გამოგვიტანს
    def test_add(self):
        # assertEqual ტესტი გვიჩვენებს იმას თუკი რა უნდა იყოს ფუნქციის შედეგი,
        # მას გადაცემა ორი პარამეტრი:...
        # 1:ფუნქციის დასახებელება.() ფრჩხილებში კი არგუმენტი რომელიც უნდა მიიღოს ფუქნციამ,
        # 2:შედეგი რაც ამ ფუქნციამ უნდა დააბრუნოს,
        # ხოლო assertEqual გვიჩვენებს ფუქნცია უდრის თუ არა შედეგს, თუ True მაშინ გამოიტანს OK
        # ხოლო თუ False არის მაშინ გამოიტანს f და გვიჩვენებს რაშია ერორი
        self.assertEqual(main.add(5, 2), 7)
        self.assertEqual(main.add(5, 2), 7)
        self.assertEqual(main.add(5, 8), 13)
        self.assertEqual(main.add(5, 4), 9)
        self.assertEqual(main.add(5, 127), 132)

    def test_sub(self):
        self.assertEqual(main.sub(5, 2), 3)
        self.assertEqual(main.sub(5, -1), 6)
        self.assertEqual(main.sub(21, 8), 13)
        # assertNotEqual კი პირიქით შებრუნებულად გვიჩვენებს
        self.assertNotEqual(main.sub(21, 1), 201)

    def test_mul(self):
        self.assertEqual(main.mul(5, 2), 10)
        self.assertEqual(main.mul(3, 2), 6)
        self.assertEqual(main.mul(7, 3), 21)
        self.assertEqual(main.mul(10, 11), 110)
        self.assertEqual(main.mul("hello", 2), "hellohello")

    def test_div(self):
        self.assertEqual(main.div(12, 2), 6)
        self.assertEqual(main.div(5, 2), 2.5)
        self.assertRaises(ValueError, main.div, 7, 0)
        # თუკი ვიყენებთ assertRaises - ამ შემთხვევაში:
        # პირველ პარამეტრად გადაცემეა იმ ერორის დასახელება რომელიც უნდა შექმნას კოდმა
        # მეორე პარამეტრია mainდან ფუნქციის დასახელება,
        # ხოლო საბოლოოდ კი პარამეტრები უნდა გადაეცეს, მაგრამ პარამეტრები არ გადაეცემა ფუნქციას ფრჩხილებში() ისევე როგორ ფუნქციის გამოძახებისას,
        # არამდე ფუნქციის შემდეგ ვუწერთ
        # ან გამოვიყვენოთ მეორე სინტაქსი: კონტექსტ მენეჯერით
        with self.assertRaises(ValueError):
            main.div(5, 0)


    def test_is_even(self):
        # assertTrue გვიბრუნებს შედეგი გამოიტანს თუ არა True-ს
        self.assertTrue(main.is_even(4))
        # მსგავსად მუშაობს assertFalse, თუკი Falseს აბრუნებს ფუქნცია მაშინ ერორზე არ გავა ტესტი
        self.assertFalse(main.is_even(11))


# კლასების / ობიექეტების ტესტინგი######################################################################################################################

class TestStudent(unittest.TestCase):
    def setUp(self):
        # იმისათვის რომ ყოველი მეთოდის გაშვებისას არ შევქმნათ ობიექტები ყოველ ჯერზე, ამისათვის setUp მეთოდში ვქმნით კლასის ობიექტებს, self კივორდით
        # და self.OBJ ით ვიძახებთ მათ ყველა მეთოდში სატესტოდ
        self.student1 = main.Student("Malkhaz", "Okriashvili", 3000)
        self.student2 = main.Student("Nika", "Okriashvili", 3200)

    def test_get_email(self):
        print("get email")
        # student1 = main.Student("Malkhaz", "Okriashvili", 3000)
        # student2 = main.Student("Nika", "Okriashvili", 3200)

        self.assertEqual(self.student1.get_email("gmail.com"), "Malkhaz.Okriashvili@gmail.com")
        self.assertEqual(self.student2.get_email("mail.com"), "Nika.Okriashvili@mail.com")
        # თუკი ობიექტში შეგვეცვლება ატრიბუტი მაშინ ტესტშიც უნდა შევცვალოთ შედეგი, წუნააღმდეგ შემთხვევაში ტესტი ვერ გაივლის
        self.student1.first_name = "Luka"
        self.assertEqual(self.student1.get_email("gmail.com"), "Luka.Okriashvili@gmail.com")


    def test_gef_full_name(self):
        print("gef_full_name")

        # student1 = main.Student("Malkhaz", "Okriashvili", 3000)
        # student2 = main.Student("Nika", "Okriashvili", 3200)

        self.assertEqual(self.student1.get_full_name, "Malkhaz Okriashvili")
        self.assertEqual(self.student2.get_full_name, "Nika Okriashvili")



    def test_discount(self):
        print("discount")

        # student1 = main.Student("Malkhaz", "Okriashvili", 3000)
        # student2 = main.Student("Nika", "Okriashvili", 3200)
        self.assertEqual(self.student1.discount(number), 2400)
        self.assertEqual(self.student2.discount(number), 2560)


    def tearDown(self):
        print("tearDown")

number = float(input("Enter a number: "))


# python .\test-main.py









if __name__ == '__main__':
    unittest.main()






