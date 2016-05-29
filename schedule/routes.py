from schedule.wsgi import api
from schedule.resources import (CreateEvent, EventInfo, EventsByDate, EventResult,
                                EventGoals, EventGoal, GoalsInfo, GoalInfo, GoalStatus,
                                StatusInfo)

api.add_resource(CreateEvent, '/event')
api.add_resource(EventInfo, '/event/<string:event_id>')
api.add_resource(EventsByDate, '/events/<string:date>')
api.add_resource(EventResult, '/event/<string:event_id>/result')
api.add_resource(EventGoals, '/event/<string:event_id>/goals')
api.add_resource(EventGoal, '/event/<string:event_id/goal/<string:goal_id>')
api.add_resource(GoalsInfo, '/goals')
api.add_resource(GoalInfo, '/goal/<string:goal_id>')
api.add_resource(GoalStatus, '/goal/<string:goal_id/status')
api.add_resource(StatusInfo, '/status/<string:status:id>')
