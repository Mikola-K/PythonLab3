from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields, validate, exceptions

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:vbrjkf16@localhost:3306/lab6'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class BankService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bank_name = db.Column(db.String(80), unique=False)
    bank_type = db.Column(db.String(80), unique=False)
    is_available = db.Column(db.Boolean, unique=False)
    interest_rate = db.Column(db.Float, unique=False)

    def __init__(self, bank_name, bank_type, is_available, interest_rate):
        self.bank_name = bank_name
        self.bank_type = bank_type
        self.is_available = is_available
        self.interest_rate = interest_rate


    def update(self, bank_name, bank_type,is_available, interest_rate):
        self.__init__(bank_name, bank_type, is_available, interest_rate)


def get_bank_service_by_id(id):
    bank_service = BankService.query.get(id)
    if bank_service is None:
        return abort(404)
    return bank_service


@app.errorhandler(exceptions.ValidationError)
def handle_exception(e):
    return e.messages, 400


class BankServiceSchema(ma.Schema):
    bank_name = fields.String(validate=validate.Length(max=80))
    bank_type = fields.String(validate=validate.Length(max=80))
    is_available = fields.Boolean()
    interest_rate = fields.Float(validate=validate.Range(0.1, 80))


bank_service_schema = BankServiceSchema()
bank_services_schema = BankServiceSchema(many=True)


@app.route("/bank_service", methods=["POST"])
def add_bank_service():
    fields = bank_service_schema.load(request.json)
    new_bank_service = BankService(**fields)

    db.session.add(new_bank_service)
    db.session.commit()

    return bank_service_schema.jsonify(new_bank_service)


@app.route("/bank_service", methods=["GET"])
def get_bank_service():
    all_bank_service = BankService.query.all()
    result = bank_services_schema.dump(all_bank_service)
    return jsonify(result)


@app.route("/bank_service/<id>", methods=["GET"])
def bank_service_detail(id):
    bank_service = get_bank_service_by_id(id)
    return bank_service_schema.jsonify(bank_service)


@app.route("/bank_service/<id>", methods=["PUT"])
def bank_service_update(id):
    bank_service = get_bank_service_by_id(id)
    fields = bank_service_schema.load(request.json)
    bank_service.update(**fields)

    db.session.commit()
    return bank_service_schema.jsonify(bank_service)


@app.route("/bank_service/<id>", methods=["DELETE"])
def bank_service_delete(id):
    bank_service = get_bank_service_by_id(id)
    db.session.delete(bank_service)
    db.session.commit()

    return bank_service_schema.jsonify(bank_service)


if __name__ == '__main__':
    app.run(debug=True)
