"""
Transaction Model
"""

from app import db
from models.user_model import UserModel

class TransactionModel(db.Model):
    """
    Transaction class, allows for transferring currency to and from accounts
    """

    __tablename__ = "transactions"
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(16, 2), nullable=False)
    to_user_id = db.Column(db.Integer, db.ForeignKey(UserModel.id))
    from_user_id = db.Column(db.Integer, db.ForeignKey(UserModel.id))

    def save_to_db(self):
        """
        Save transaction to database
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_balance_for_user_id(cls, user_id):
        """
        Get balance for a user
        """
        from_transactions = cls.query.filter_by(from_user_id=user_id)
        to_transactions = cls.query.filter_by(to_user_id=user_id)
        print(from_transactions)
        print(to_transactions)
        return 0
