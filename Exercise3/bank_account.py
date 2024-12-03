class BankAccount:
    def __init__(self, account_holder, initial_balance=0, currency='JPY'):
        # 口座所有者の名前を保存
        self.account_holder = account_holder
        # 各通貨ごとの残高を管理する辞書
        self.balances = {currency: initial_balance}
        # 為替レートを管理する辞書（仮のレート）
        self.exchange_rates = {
            'JPY': 1.0,       # 日本円
            'USD': 0.0091,    # 米ドル
            'EUR': 0.0077     # ユーロ
        }

    def deposit(self, amount, currency='JPY'):
        # 入金処理
        if currency in self.balances:
            self.balances[currency] += amount
        else:
            self.balances[currency] = amount

    def withdraw(self, amount, currency='JPY'):
        # 出金処理
        if currency in self.balances and self.balances[currency] >= amount:
            self.balances[currency] -= amount
            return amount
        else:
            raise ValueError('Insufficient balance.')

    def get_balance(self, currency='JPY'):
        # 指定された通貨の残高を取得
        return self.balances.get(currency, 0)

    def get_total_balance_in_jpy(self):
        # 全ての通貨の残高を日本円に換算して合計を取得
        total = 0
        for curr, balance in self.balances.items():
            # 各通貨の残高を日本円に換算
            rate = self.exchange_rates.get(curr)
            if rate:
                total += balance / rate
            else:
                raise ValueError(f'Cannot find exchange rate for {curr} .')
        return total

    def transfer(self, amount, to_account, currency='JPY'):
        # 他の口座へ振込
        self.withdraw(amount, currency)
        to_account.deposit(amount, currency)

    def update_exchange_rate(self, currency, rate):
        # 為替レートの更新
        self.exchange_rates[currency] = rate

    def __str__(self):
        # 口座情報の文字列表現
        balances_str = ', '.join([f"{curr}: {amt}" for curr, amt in self.balances.items()])
        return f"Account holder: {self.account_holder}, Balance: {balances_str}"
