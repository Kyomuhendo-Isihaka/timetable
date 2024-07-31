# from django.core.management.base import BaseCommand
# from django.core.exceptions import ValidationError
# from store.models import Timetable, CourseSchedule, Course, TimeSlot, Room, Staff

# class Command(BaseCommand):
#     help = 'Generates a timetable'

#     def add_arguments(self, parser):
#         parser.add_argument('program_id', type=int)
#         parser.add_argument('year', type=str)

#     def handle(self, *args, **kwargs):
#         program_id = kwargs['program_id']
#         year = kwargs['year']

#         # Check if timetable already exists
#         existing_timetable = Timetable.objects.filter(program_id=program_id, year=year).first()
#         if existing_timetable:
#             self.stdout.write(f"Timetable already exists for Program ID: {program_id}, Year: {year}, ID: {existing_timetable.id}")
#             return

#         try:
#             timetable = Timetable.objects.create(program_id=program_id, year=year)
#             self.stdout.write(f"Timetable created: True, ID: {timetable.id}")
#         except Exception as e:
#             self.stdout.write(f"Timetable created: False, Error: {str(e)}")
#             return

#         courses = Course.objects.filter(program_id=program_id, course_year=year)
#         self.stdout.write(f"All Courses: {list(courses)}")

#         timeslots = TimeSlot.objects.all()
#         rooms = Room.objects.all()
#         staff = Staff.objects.all()

#         self.stdout.write(f"Timeslots: {list(timeslots)}")
#         self.stdout.write(f"Rooms: {list(rooms)}")
#         self.stdout.write(f"Staff: {list(staff)}")

#         for course in courses:
#             self.stdout.write(f"Assigning course: {course.course_name}")

#             assigned = False
#             for day in TimeSlot.DAY_CHOICES:
#                 day_name = day[0]
#                 day_timeslots = timeslots.filter(day=day_name)
#                 self.stdout.write(f"Checking day: {day_name}")
#                 self.stdout.write(f"Timeslots for {day_name}: {list(day_timeslots)}")

#                 for timeslot in day_timeslots:
#                     self.stdout.write(f"Checking timeslot: {timeslot}")
#                     for room in rooms:
#                         self.stdout.write(f"Checking room: {room.room_name}")
#                         for lecturer in staff:
#                             self.stdout.write(f"Checking lecturer: {lecturer.username}")
#                             try:
#                                 CourseSchedule.objects.create(
#                                     timetable=timetable,
#                                     course=course,
#                                     room=room,
#                                     timeslot=timeslot,
#                                     staff=lecturer
#                                 )
#                                 self.stdout.write(f"Assigned {course.course_name} to {room.room_name} at {timeslot} with {lecturer.username}")
#                                 assigned = True
#                                 break
#                             except ValidationError as e:
#                                 self.stdout.write(f"Could not assign {course.course_name} due to conflict: {str(e)}")
#                         if assigned:
#                             break
#                     if assigned:
#                         break
#                 if assigned:
#                     break

#             if not assigned:
#                 self.stdout.write(f"Could not assign course {course.course_name} due to conflicts.")


from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from store.models import Timetable, CourseSchedule, Course, TimeSlot, Room, Staff

class Command(BaseCommand):
    help = 'Generates a timetable'

    def add_arguments(self, parser):
        parser.add_argument('program_id', type=int)
        parser.add_argument('year', type=str)

    def handle(self, *args, **kwargs):
        program_id = kwargs['program_id']
        year = kwargs['year']

        # Check if timetable already exists
        existing_timetable = Timetable.objects.filter(program_id=program_id, year=year).first()
        if existing_timetable:
            self.stdout.write(f"Timetable already exists for Program ID: {program_id}, Year: {year}, ID: {existing_timetable.id}")
            return

        try:
            timetable = Timetable.objects.create(program_id=program_id, year=year)
            self.stdout.write(f"Timetable created: True, ID: {timetable.id}")
        except Exception as e:
            self.stdout.write(f"Timetable created: False, Error: {str(e)}")
            return

        courses = Course.objects.filter(program_id=program_id, course_year=year)
        self.stdout.write(f"All Courses: {list(courses)}")

        timeslots = TimeSlot.objects.all()
        rooms = Room.objects.all()
        staff = Staff.objects.all()

        self.stdout.write(f"Timeslots: {list(timeslots)}")
        self.stdout.write(f"Rooms: {list(rooms)}")
        self.stdout.write(f"Staff: {list(staff)}")

        for course in courses:
            self.stdout.write(f"Assigning course: {course.course_name}")

            assigned = False
            for day in TimeSlot.DAY_CHOICES:
                day_name = day[0]
                day_timeslots = timeslots.filter(day=day_name)
                self.stdout.write(f"Checking day: {day_name}")
                self.stdout.write(f"Timeslots for {day_name}: {list(day_timeslots)}")

                daily_schedule_count = 0

                for timeslot in day_timeslots:
                    self.stdout.write(f"Checking timeslot: {timeslot}")
                    for room in rooms:
                        self.stdout.write(f"Checking room: {room.room_name}")
                        for lecturer in staff:
                            self.stdout.write(f"Checking lecturer: {lecturer.username}")
                            try:
                                CourseSchedule.objects.create(
                                    timetable=timetable,
                                    course=course,
                                    room=room,
                                    timeslot=timeslot,
                                    staff=lecturer
                                )
                                self.stdout.write(f"Assigned {course.course_name} to {room.room_name} at {timeslot} with {lecturer.username}")
                                assigned = True
                                daily_schedule_count += 1
                                if daily_schedule_count >= 2:
                                    break  # Break out of the lecturer loop if two schedules are assigned
                            except ValidationError as e:
                                self.stdout.write(f"Could not assign {course.course_name} due to conflict: {str(e)}")
                        if daily_schedule_count >= 2:
                            break  # Break out of the room loop if two schedules are assigned
                    if daily_schedule_count >= 2:
                        break  # Break out of the timeslot loop if two schedules are assigned
                if daily_schedule_count >= 2:
                    break  # Break out of the day loop if two schedules are assigned

            if not assigned:
                self.stdout.write(f"Could not assign course {course.course_name} due to conflicts.")
