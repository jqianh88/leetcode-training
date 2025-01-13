'''
Problem: Design a payment system

You need to design a payment system that supports multiple types of payments: credit card, debit card, and PayPal. The system should allow for:

Making a payment.
Checking the payment status.
Handling different types of transactions (success or failure).
Requirements:

Implement classes for each payment type (e.g., CreditCardPayment, DebitCardPayment, PaypalPayment).
Apply the SOLID principles to design the system.
Follow-Up:

How would you extend the system to support additional payment methods (like bank transfers or cryptocurrency)?
What improvements would you make to make the system more extensible and maintainable?

'''

# from abc import ABC, abstractmethod
# import datetime
# from uuid import UUID, uuid4

# class Payment(ABC):
#     def __init__(self, payment_type):
#         self.payment_type = payment_type

#     @abstractmethod
#     def make_payment(self, payment_info: dict) -> 'Transaction':
#         pass

#     def is_valid_transaction(self) -> bool:
#         """
#         Common validation logic, e.g., checking for valid card number or balance.
#         """
#         raise NotImplementedError("This method should be implemented by the subclass.")

# class CreditCardPayment(Payment):
#     def __init__(self, credit_card_type: str, credit_card_number: str, credit_card_expiration_date: str):
#         super().__init__(payment_type="credit")
#         self.credit_card_type = credit_card_type
#         self.credit_card_number = credit_card_number
#         self.credit_card_expiration_date = credit_card_expiration_date
#         self.is_valid = False

#     def make_payment(self, payment_info: dict) -> 'Transaction':
#         self.credit_card_number = payment_info['credit_card_number']
#         self.credit_card_expiration_date = payment_info['credit_card_expiration_date']
#         self.is_valid = self.is_valid_transaction()

#         status = "success" if self.is_valid else "failure"
#         return Transaction(status=status)

#     def is_valid_transaction(self) -> bool:
#         """
#         Validate the credit card number and expiration date.
#         """
#         if len(self.credit_card_number) == 16 and self.credit_card_expiration_date > str(datetime.datetime.now(datetime.timezone.utc)):
#             return True
#         return False


# class DebitCardPayment(Payment):
#     def __init__(self, debit_card_type: str, debit_card_balance: float):
#         super().__init__(payment_type="debit")
#         self.debit_card_type = debit_card_type
#         self.debit_card_balance = debit_card_balance

#     def make_payment(self, payment_info: dict) -> 'Transaction':
#         self.debit_card_balance = payment_info['debit_card_balance']
#         self.is_valid = self.is_valid_transaction()

#         status = "success" if self.is_valid else "failure"
#         return Transaction(status=status)

#     def is_valid_transaction(self) -> bool:
#         if self.debit_card_balance > 0:
#             return True
#         return False


# class PaypalPayment(Payment):
#     def __init__(self, paypal_balance: float, paypal_id: str):
#         super().__init__(payment_type="paypal")
#         self.paypal_balance = paypal_balance
#         self.paypal_id = paypal_id

#     def make_payment(self, payment_info: dict) -> 'Transaction':
#         self.paypal_balance = payment_info['paypal_balance']
#         self.paypal_id = payment_info['paypal_id']
#         self.is_valid = self.is_valid_transaction()

#         status = "success" if self.is_valid else "failure"
#         return Transaction(status=status)

#     def is_valid_transaction(self) -> bool:
#         if self.paypal_balance > 0:
#             return True
#         return False


# class BankTransferPayment(Payment):
#     def __init__(self, bank_balance: float, bank_account: str):
#         super().__init__(payment_type="bank")
#         self.bank_balance = bank_balance
#         self.bank_account = bank_account

#     def make_payment(self, payment_info: dict) -> 'Transaction':
#         self.bank_balance = payment_info['bank_balance']
#         self.bank_account = payment_info['bank_account']
#         self.is_valid = self.is_valid_transaction()

#         status = "success" if self.is_valid else "failure"
#         return Transaction(status=status)

#     def is_valid_transaction(self) -> bool:
#         if self.bank_balance > 0:
#             return True
#         return False


# class CryptoPayment(Payment):
#     def __init__(self, crypto_balance: float, crypto_account: str):
#         super().__init__(payment_type="crypto")
#         self.crypto_balance = crypto_balance
#         self.crypto_account = crypto_account

#     def make_payment(self, payment_info: dict) -> 'Transaction':
#         self.crypto_balance = payment_info['crypto_balance']
#         self.crypto_account = payment_info['crypto_account']
#         self.is_valid = self.is_valid_transaction()

#         status = "success" if self.is_valid else "failure"
#         return Transaction(status=status)

#     def is_valid_transaction(self) -> bool:
#         if self.crypto_balance > 0:
#             return True
#         return False


# class Transaction:
#     def __init__(self, status: str):
#         self.transaction_id = uuid4()
#         self.transaction_status = status
#         self.transaction_time = datetime.datetime.now(datetime.timezone.utc)

#     def get_transaction_id(self):
#         return self.transaction_id

#     def get_transaction_status(self):
#         return self.transaction_status

#     def get_transaction_time(self):
#         return self.transaction_time

#     def get_transaction(self):
#         return {
#             "transaction_id": self.transaction_id,
#             "transaction_status": self.transaction_status,
#             "transaction_time": self.transaction_time
#         }


# if __name__ == "__main__":
#     credit_card_payment = CreditCardPayment(credit_card_type="Visa", credit_card_number="1234567890123456", credit_card_expiration_date="2024-12-31")
#     payment_info = {
#         'credit_card_number': "1234567890123456",
#         'credit_card_expiration_date': "2024-12-31"
#     }
#     transaction = credit_card_payment.make_payment(payment_info)

#     # Get transaction status
#     print(transaction.get_transaction_id()) # created uuid
#     print(transaction.get_transaction_status())  # success or failure
#     print(transaction.get_transaction_time())    # The time of the transaction
#     print(transaction.get_transaction())




#### Improved Version with below suggestions

from abc import ABC, abstractmethod
import datetime
from uuid import uuid4


from abc import ABC, abstractmethod
import datetime

# Base Payment class with common validation logic
class Payment(ABC):
    def __init__(self, payment_info: dict):
        self.payment_info = payment_info  # Payment details (e.g., credit card info, balance)

    @abstractmethod
    def make_payment(self) -> 'Transaction':
        """
        Abstract method for processing the payment. Each payment method will implement this.
        """
        pass

    def is_valid_transaction(self) -> bool:
        """
        This method validates common payment-related checks like payment type and delegates
        detailed validation to subclasses.
        """
        if self.is_valid_payment_type():
            return self.perform_payment_specific_validation()
        return False

    def is_valid_payment_type(self) -> bool:
        """Checks whether the payment info has a valid payment type"""
        valid_payment_types = ['credit', 'debit', 'paypal', 'bank', 'crypto']
        return self.payment_info.get('payment_type') in valid_payment_types

    def perform_payment_specific_validation(self) -> bool:
        """Delegates the actual validation to the specific payment method"""
        raise NotImplementedError("This method should be implemented by the subclass.")

    # Utility methods for common validations
    def is_credit_card_valid(self) -> bool:
        """Common validation for credit card"""
        card_number = self.payment_info.get('credit_card_number', '')
        expiration_date = self.payment_info.get('credit_card_expiration_date', '')
        if len(card_number) == 16 and expiration_date > str(datetime.datetime.now(datetime.timezone.utc)):
            return True
        return False

    def is_debit_card_valid(self) -> bool:
        """Common validation for debit cards"""
        balance = self.payment_info.get('debit_card_balance', 0)
        if balance >= self.payment_info.get('payment', 0):
            return True
        return False

    def is_paypal_valid(self) -> bool:
        """Common validation for PayPal"""
        balance = self.payment_info.get('paypal_balance', 0)
        if balance >= self.payment_info.get('payment', 0):
            return True
        return False


# Transaction class that stores the status, time, and reason of the transaction
class Transaction:
    def __init__(self, status: str, reason: str = None):
        self.transaction_id = uuid4()
        self.transaction_status = status
        self.transaction_time = datetime.datetime.now(datetime.timezone.utc)
        self.reason = reason

    def get_transaction_id(self):
        return self.transaction_id

    def get_transaction_status(self):
        return self.transaction_status

    def get_transaction_time(self):
        return self.transaction_time

    def get_transaction(self):
        return {
            "transaction_id": self.transaction_id,
            "transaction_status": self.transaction_status,
            "transaction_time": self.transaction_time,
            "reason": self.reason
        }


# Credit Card Payment subclass
class CreditCardPayment(Payment):
    def __init__(self, payment_info: dict):
        super().__init__(payment_info)

    def make_payment(self) -> 'Transaction':
        if self.is_valid_transaction():
            # Simulate processing the payment
            return Transaction(status="success")
        return Transaction(status="failure", reason="Invalid credit card or expiration date")

    def perform_payment_specific_validation(self) -> bool:
        return self.is_credit_card_valid()


# Debit Card Payment subclass
class DebitCardPayment(Payment):
    def __init__(self, payment_info: dict):
        super().__init__(payment_info)

    def make_payment(self) -> 'Transaction':
        if self.is_valid_transaction():
            # Simulate processing the payment
            return Transaction(status="success")
        return Transaction(status="failure", reason="Insufficient balance")

    def perform_payment_specific_validation(self) -> bool:
        return self.is_debit_card_valid()


# PayPal Payment subclass
class PaypalPayment(Payment):
    def __init__(self, payment_info: dict):
        super().__init__(payment_info)

    def make_payment(self) -> 'Transaction':
        if self.is_valid_transaction():
            # Simulate processing the payment
            return Transaction(status="success")
        return Transaction(status="failure", reason="Insufficient PayPal balance")

    def perform_payment_specific_validation(self) -> bool:
        return self.is_paypal_valid()


# Bank Transfer Payment subclass
class BankTransferPayment(Payment):
    def __init__(self, payment_info: dict):
        super().__init__(payment_info)

    def make_payment(self) -> 'Transaction':
        if self.is_valid_transaction():
            # Simulate processing the payment
            return Transaction(status="success")
        return Transaction(status="failure", reason="Insufficient funds")

    def perform_payment_specific_validation(self) -> bool:
        return self.is_paypal_valid()  # Use any specific bank transfer validation


# Crypto Payment subclass
class CryptoPayment(Payment):
    def __init__(self, payment_info: dict):
        super().__init__(payment_info)

    def make_payment(self) -> 'Transaction':
        if self.is_valid_transaction():
            # Simulate processing the payment
            return Transaction(status="success")
        return Transaction(status="failure", reason="Insufficient crypto balance")

    def perform_payment_specific_validation(self) -> bool:
        return self.is_paypal_valid()  # Use any specific crypto validation


if __name__ == '__main__':

    # Example usage

    # Credit Card payment info
    credit_card_info = {
        'payment_type': 'credit',
        'credit_card_number': "1234567890123456",
        'credit_card_expiration_date': "2025-12-31",
        'payment': 100  # Payment amount
    }

    # Initialize CreditCardPayment with payment_info
    credit_card_payment = CreditCardPayment(credit_card_info)

    # Process the payment
    transaction = credit_card_payment.make_payment()

    # Output the result
    print(transaction.get_transaction_id())  # uuid4 transaction_id
    print(transaction.get_transaction_status())  # success or failure
    print(transaction.get_transaction_time())    # The time of the transaction




'''
Your solution demonstrates a solid understanding of object-oriented principles and is a good foundation for implementing a payment system. However, when preparing for a final loop interview at Amazon (or similar high-level software engineering interviews), there are a few things that they would typically look for beyond the basic correctness of your solution. Here's how your answer aligns with Amazon's expectations:

Strengths of Your Approach:
Solid Object-Oriented Design:

You correctly used abstract classes and inheritance (with Payment as the base class and the specific payment types inheriting from it). This demonstrates an understanding of how to structure the problem using OOP principles.
You created distinct payment types (CreditCardPayment, DebitCardPayment, etc.), which is good for modularity and extensibility. This aligns with Amazon's emphasis on building scalable and maintainable systems.
Separation of Concerns:

By separating the payment logic and transaction logic into distinct classes (Payment and Transaction), you're following the Single Responsibility Principle (SRP). This is an important design principle that Amazon highly values.
Transaction Handling:

You correctly encapsulated the payment result (success/failure) within a Transaction class, which makes sense in terms of organizing the system and keeping it flexible for future changes.
Opportunities for Improvement (Things Amazon Would Likely Expect):
Code Duplication:

What you did: You repeated the make_payment and is_valid_transaction logic in each subclass (CreditCardPayment, DebitCardPayment, etc.), which works but introduces code duplication.
Amazon Expectation: In Amazon interviews, reducing duplication and adhering to clean code principles is crucial. You could improve this by refactoring the common logic into a base class or a utility class. Specifically:
Common validation logic (e.g., checking account number length, expiration date, balance) can be abstracted to avoid redundancy.
A better solution might use a helper function or strategy pattern for validation that all subclasses can share.
Suggestion: Refactor the is_valid_transaction method to be more abstract and reusable, possibly by using helper methods that can be used across different payment types (e.g., validate card number, balance checks).

Design for Flexibility & Extensibility:

What you did: You extended the system to multiple payment types, which is good.
Amazon Expectation: Amazon typically wants to see a highly extensible and flexible design. For example:
If you were to add another payment method (e.g., Mobile Payment, Apple Pay), the current system would require some modifications in each payment class.
A more scalable solution might use composition (e.g., using interfaces or strategy patterns) instead of inheritance in some cases.
Suggestion: Use the strategy pattern to decouple payment methods from the payment processing logic. You could create a PaymentProcessor interface/abstract class with a process_payment() method and have specific payment classes implement this interface. This way, adding new payment types would be easier without modifying existing code.

Transaction Handling and Status Reporting:

What you did: You used the Transaction class to store the status of the transaction.
Amazon Expectation: In a real-world scenario, Amazon would likely expect you to handle edge cases and robust error handling. For example:
What happens when a transaction is invalid due to insufficient funds? How does your system handle retries, rollbacks, or different error codes?
What happens if a payment request fails midway (e.g., due to network errors)?
Suggestion: Consider implementing transaction retry logic, failure handling, and potentially compensating transactions (for example, to reverse a failed transaction).

Performance and Scalability Considerations:

What you did: The design is focused on correctness, which is great.
Amazon Expectation: Amazon places a lot of emphasis on performance and scalability, especially in high-demand systems. For example:
How does this system handle high traffic? If there were millions of transactions per day, how would you ensure the system scales?
Consider introducing a caching mechanism or optimizing the validation logic for high throughput.
How would you persist transactions and ensure atomicity (ACID properties)? Amazon may expect some discussion of distributed systems and databases.
Code Readability and Clarity:

What you did: Your code is fairly readable, but some comments explaining the higher-level design (like transaction handling, validation, etc.) could improve clarity.
Amazon Expectation: At Amazon, clear, self-explanatory code and excellent documentation are highly valued. While you’ve included basic comments, a more detailed explanation of the design decisions (why certain methods were abstracted, how the validation works, how the payment process flows) would be important in interviews.
Testing and Edge Cases:

What you did: The current solution does not include tests or edge case handling.
Amazon Expectation: Amazon interviews often involve thinking about testability and writing testable code. You would be expected to:
Write unit tests for the Payment and Transaction classes.
Consider edge cases (e.g., invalid payment details, expired cards, insufficient balance).
Ensure the system handles exceptions gracefully.
Suggestion: Consider writing unit tests for each payment method and validating the transaction outcomes in different scenarios (success, failure, invalid input).

Conclusion:
Your approach is close to what Amazon would expect in a final loop interview, but to make it more polished and aligned with their expectations, focus on:

Refactoring to reduce code duplication and increase flexibility.
Handling failure scenarios more robustly (e.g., transaction retries, error handling).
Designing for scalability and testability.
Explaining your design decisions more clearly.
Amazon places a significant emphasis on clean, extensible code, performance, and scalability in their final interviews, so by incorporating these suggestions, you’ll be able to present a solution that aligns with their expectations.



Additional Considerations:
Edge Case Handling: In a real-world system, you might need to handle additional edge cases, such as:

Network issues: What if a payment fails due to a network issue? You might need retry logic.
Partial payments: If part of the payment goes through but not the full amount, how should you handle this?
Persisting Transactions: In a full system, you would likely persist each Transaction to a database for historical tracking and auditability. This means that the Transaction object could be part of a larger transaction management system.

Error Handling: Ensure that all failures, timeouts, and edge cases are captured in the Transaction class, possibly including more detailed error codes or messages to improve debugging and logging.
    '''