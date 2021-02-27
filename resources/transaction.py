"""
Transaction API
"""

from flask_jwt_extended import current_user, jwt_required
from flask_restful import Resource, reqparse
from models.transaction_model import TransactionModel
from models.user_model import UserModel

transaction_parser = reqparse.RequestParser()
transaction_parser.add_argument(
    "from_user_id", type=int, help="from_user_id cannot be blank", required=True)
transaction_parser.add_argument(
    "to_user_id", type=int, help="to_user_id cannot be blank", required=True)
transaction_parser.add_argument(
    "amount", type=float, help="amount cannot be blank", required=True)


class Transaction(Resource):
    """
    Move currency from one account to another
    """

    @jwt_required()
    def post(self):
        """
        Create a new transaction. Check that the auth'd user is sending a
        positive amount of money to an existing user, and that they have enough
        money in their account to complete the transaction
        """
        data = transaction_parser.parse_args()
        from_user_id = data["from_user_id"]
        to_user_id = data["to_user_id"]
        amount = data["amount"]

        if (current_user.id != from_user_id or from_user_id == to_user_id or amount <= 0):
            return {"message": "invalid transaction details"}, 400

        from_user = UserModel.find_by_id(from_user_id)
        to_user = UserModel.find_by_id(to_user_id)

        if (from_user is None or to_user is None):
            return {"message": "invalid transaction details"}, 400

        new_transaction = TransactionModel(
            from_user_id=from_user_id,
            to_user_id=to_user_id,
            amount=amount,
        )

        try:
            new_transaction.save_to_db()

            return {
                "message": f"Sent {new_transaction.amount} from {from_user.username} to {to_user.username}",
            }

        except Exception as exception:
            print(exception)
            return {"message": "Something went wrong"}, 500
