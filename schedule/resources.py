from flask_restful import Resource


class CreateEvent(Resource):
    def post(self):
        pass


class EventInfo(Resource):
    def get(self, event_id):
        pass

    def put(self, event_id):
        pass

    def delete(self, event_id):
        pass


class EventsByDate(Resource):
    def get(self, date):
        pass


class EventResult(Resource):
    def get(self, event_id):
        pass

    def put(self, event_id):
        pass

    def post(self, event_id):
        pass

    def delete(self, event_id):
        pass


class EventGoals(Resource):
    def get(self, event_id):
        pass

    def put(self, event_id):
        pass


class EventGoal(Resource):
    def delete(self, event_id, goal_id):
        pass


class GoalsInfo(Resource):
    def get(self):
        pass

    def post(self):
        pass


class GoalInfo(Resource):
    def get(self, goal_id):
        pass

    def put(self, goal_id):
        pass

    def delete(self, goal_id):
        pass


class GoalStatus(Resource):
    def get(self, goal_id):
        pass

    def post(self, goal_id):
        pass


class StatusInfo(Resource):
    def put(self, status_id):
        pass

    def delete(self, status_id):
        pass
