class Participant:
    def __init__(self, id, name, email, phone, team_id, role, password_hash):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.team_id = team_id
        self.role = role
        self.password_hash = password_hash
