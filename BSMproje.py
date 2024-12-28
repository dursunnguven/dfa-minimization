class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        # DFA'yı tanımlamak için başlangıç özelliklerini belirliyoruz
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def remove_unreachable_states(self):
        # Ulaşılabilir durumları belirlemek için bir set ve ziyaret listesi kullanıyoruz
        reachable = set()
        to_visit = [self.start_state]

        while to_visit:
            current_state = to_visit.pop()
            if current_state not in reachable:
                reachable.add(current_state)
                for symbol in self.alphabet:
                    # Geçiş fonksiyonunu kullanarak sonraki durumu belirliyoruz
                    next_state = self.transition_function.get((current_state, symbol))
                    if next_state and next_state not in reachable:
                        to_visit.append(next_state)

        # Ulaşılmayan durumları ve bu durumlara ait geçişleri kaldırıyoruz
        self.states = [state for state in self.states if state in reachable]
        self.transition_function = {
            key: value
            for key, value in self.transition_function.items()
            if key[0] in reachable and value in reachable
        }
        self.accept_states = [state for state in self.accept_states if state in reachable]

    def minimize(self):
        # 1. Adım: Kabul ve kabul olmayan durumları başlangıçta farklı gruplara ayırıyoruz
        partitions = [set(self.accept_states), set(self.states) - set(self.accept_states)]

        while True:
            new_partitions = []
            for group in partitions:
                # Her grubu daha küçük alt gruplara ayırıyoruz
                sub_partitions = self.split_group(group, partitions)
                new_partitions.extend(sub_partitions)

            # Eğer bölünmeler sabitlenmişse döngüden çıkıyoruz
            if new_partitions == partitions:
                break

            partitions = new_partitions

        # 2. Adım: Eşdeğer durumları birleştiriyoruz
        new_states = [frozenset(group) for group in partitions]
        new_transition_function = {}
        state_mapping = {
            state: f"State_{i}"
            for i, new_state in enumerate(new_states)
            for state in new_state
        }

        # Yeni geçiş fonksiyonunu oluşturuyoruz
        for (state, symbol), target in self.transition_function.items():
            new_transition_function[(state_mapping[state], symbol)] = state_mapping[target]

        # Yeni başlangıç ve kabul durumlarını belirliyoruz
        new_start_state = state_mapping[self.start_state]
        new_accept_states = {state_mapping[state] for state in self.accept_states}

        # Yeni özellikleri atıyoruz
        self.states = list(set(state_mapping.values()))
        self.transition_function = new_transition_function
        self.start_state = new_start_state
        self.accept_states = new_accept_states

    def split_group(self, group, partitions):
        # Grupları bölmek için her durumun geçişlerini kontrol ediyoruz
        sub_partitions = {}
        for state in group:
            key = tuple(
                # Durumun geçiş yaptığı diğer durumun hangi grupta olduğunu belirliyoruz
                next((i for i, part in enumerate(partitions) if self.transition_function.get((state, symbol)) in part), None)
                for symbol in self.alphabet
            )
            sub_partitions.setdefault(key, set()).add(state)

        # Alt grupları döndürüyoruz
        return list(sub_partitions.values())

    def __str__(self):
        # DFA'nın okunabilir bir temsilini döndürüyoruz
        return (
            f"Durumlar: {self.states}\n"
            f"Alfabe: {self.alphabet}\n"
            f"Geçiş Fonksiyonu: {self.format_transition_function()}\n"
            f"Başlangıç Durumu: {self.start_state}\n"
            f"Kabul Durumları: {self.accept_states}"
        )

    def format_transition_function(self):
        # Geçiş fonksiyonunu okunabilir bir tablo gibi gösteriyoruz
        formatted = []
        for (state, symbol), target in self.transition_function.items():
            formatted.append(f"({state}, {symbol}) -> {target}")
        return "\n".join(formatted)

def user_defined_dfa():
    # Kullanıcıdan DFA bileşenlerini alıyoruz
    states = input("Durumları virgülle ayırarak girin: ").split(',')
    alphabet = input("Alfabe sembollerini virgülle ayırarak girin: ").split(',')
    transition_function = {}
    print("Geçiş fonksiyonunu şu formatta girin 'durum,sembol -> hedef_durum' (bitirmek için 'done' yazın):")
    while True:
        transition = input()
        if transition == 'done':
            break
        key, value = transition.split(' -> ')
        state, symbol = key.split(',')
        transition_function[(state, symbol)] = value
    start_state = input("Başlangıç durumunu girin: ")
    accept_states = input("Kabul durumlarını virgülle ayırarak girin: ").split(',')
    return DFA(states, alphabet, transition_function, start_state, accept_states)

def predefined_dfa():
    # Örnek bir DFA tanımlıyoruz
    states = ['q0', 'q1', 'q2', 'q3']  # DFA'nın durumları
    alphabet = ['0', '1']  # DFA'nın alfabesi
    transition_function = {  # DFA'nın geçiş fonksiyonu
        ('q0', '0'): 'q1',
        ('q0', '1'): 'q2',
        ('q1', '0'): 'q0',
        ('q1', '1'): 'q3',
        ('q2', '0'): 'q3',
        ('q2', '1'): 'q0',
        ('q3', '0'): 'q3',
        ('q3', '1'): 'q3',
    }
    start_state = 'q0'  # Başlangıç durumu
    accept_states = ['q3']  # Kabul durumları
    return DFA(states, alphabet, transition_function, start_state, accept_states)

if __name__ == "__main__":
    while True:
        print("Bir seçenek seçin:")
        print("1. Kendi DFA'nızı tanımlayın")
        print("2. Önceden tanımlı DFA'yı kullanın")
        print("3. Programdan çıkış")
        choice = input("Seçiminizi yapın (1, 2 veya 3): ")

        if choice == '1':
            dfa = user_defined_dfa()
        elif choice == '2':
            dfa = predefined_dfa()
        elif choice == '3':
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
            continue

        print("\nOrijinal DFA:")
        print(dfa)

        dfa.remove_unreachable_states()
        print("\nUlaşılmayan durumlar kaldırıldıktan sonra:")
        print(dfa)

        dfa.minimize()
        print("\nMinimize edilmiş DFA:")
        print(dfa)
