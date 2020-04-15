"""
purpose of the schema is to represent kudo data and serve as reference to validate incoming request payload
"""

from marshmallow import Schema, fields

class GithubRepoSchema(Schema):
    id = fields.Int(required=True)
    repo_name = fields.Str()
    full_name = fields.Str()
    description = fields.Str()

class KudoSchema(GithubRepoSchema):
    user_id = fields.Email(required=True)