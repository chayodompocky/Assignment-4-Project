class Dictionary:
    def __init__(self):
        self.words = []
        self.current_index = -1

    def add_word(self, english, thai, word_type):
        word = {
            'english': english,
            'thai': thai,
            'type': word_type
        }
        self.words.append(word)

    def get_word(self, english):
        for word in self.words:
            if word['english'] == english:
                return word
        return None

    def update_word(self, english, thai=None, word_type=None):
        word = self.get_word(english)
        if word:
            if thai:
                word['thai'] = thai
            if word_type:
                word['type'] = word_type
            return True
        return False

    def delete_word(self, english):
        word = self.get_word(english)
        if word:
            self.words.remove(word)
            return True
        return False

    def display_all_words(self):
        for word in self.words:
            print(f"{word['english']} ({word['thai']}) - {word['type']}")

    def get_next_word(self):
        if self.current_index < len(self.words) - 1:
            self.current_index += 1
            return self.words[self.current_index]
        else:
            print("No next word.")
            return None

    def get_previous_word(self):
        if self.current_index > 0:
            self.current_index -= 1
            return self.words[self.current_index]
        else:
            print("No previous word.")
            return None


def main():
    dictionary = Dictionary()

    # เพิ่มคำศัพท์ตั้งต้น
    initial_words = [
        ('hello', 'สวัสดี', 'greeting'),
        ('world', 'โลก', 'noun'),
        ('python', 'ไพทอน', 'programming language'),
        ('computer', 'คอมพิวเตอร์', 'noun'),
        ('book', 'หนังสือ', 'noun'),
        ('table', 'โต๊ะ', 'noun'),
        ('run', 'วิ่ง', 'verb'),
        ('happy', 'มีความสุข', 'adjective'),
        ('blue', 'สีน้ำเงิน', 'color'),
        ('apple', 'แอปเปิล', 'fruit'),
        ('moon', 'ดวงจันทร์', 'noun'),
        ('ocean', 'มหาสมุทร', 'noun'),
        ('music', 'เพลง', 'noun'),
        ('sun', 'ตะวัน', 'noun'),
        ('green', 'สีเขียว', 'color'),
        ('learn', 'เรียนรู้', 'verb'),
        ('family', 'ครอบครัว', 'noun'),
        ('friend', 'เพื่อน', 'noun'),
        ('happy', 'มีความสุข', 'adjective'),  # ซ้ำ
        ('coding', 'การเขียนโค้ด', 'noun'),
    ]

    for word_data in initial_words:
        dictionary.add_word(*word_data)

    while True:
        print("\nDictionary Menu:")
        print("1. Add Word")
        print("2. Get Word")
        print("3. Update Word")
        print("4. Delete Word")
        print("5. Display All Words")
        print("6. Get Next Word")
        print("7. Get Previous Word")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            english = input("Enter English word: ")
            thai = input("Enter Thai translation: ")
            word_type = input("Enter word type: ")
            dictionary.add_word(english, thai, word_type)
            print("Word added successfully!")

        elif choice == '2':
            english = input("Enter English word to retrieve: ")
            word = dictionary.get_word(english)
            if word:
                print(f"{word['english']} ({word['thai']}) - {word['type']}")
            else:
                print("Word not found.")

        elif choice == '3':
            english = input("Enter English word to update: ")
            thai = input("Enter new Thai translation (press Enter to keep the same): ")
            word_type = input("Enter new word type (press Enter to keep the same): ")
            if dictionary.update_word(english, thai, word_type):
                print("Word updated successfully!")
            else:
                print("Word not found.")

        elif choice == '4':
            english = input("Enter English word to delete: ")
            if dictionary.delete_word(english):
                print("Word deleted successfully!")
            else:
                print("Word not found.")

        elif choice == '5':
            dictionary.display_all_words()

        elif choice == '6':
            next_word = dictionary.get_next_word()
            if next_word:
                print(f"Next word: {next_word['english']} ({next_word['thai']}) - {next_word['type']}")

        elif choice == '7':
            previous_word = dictionary.get_previous_word()
            if previous_word:
                print(f"Previous word: {previous_word['english']} ({previous_word['thai']}) - {previous_word['type']}")

        elif choice == '8':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
