# from django.core.management.base import BaseCommand
# from django.core.exceptions import ValidationError
# from store.models import Course, Room, TimeSlot, Staff, Timetable, CourseSchedule, Program

# class Command(BaseCommand):
#     help = 'Auto-generate timetable for a given program and year'

#     def add_arguments(self, parser):
#         parser.add_argument('program_id', type=int, help='The ID of the program')
#         parser.add_argument('year', type=int, help='The year of the program')

#     def handle(self, *args, **kwargs):
#         program_id = kwargs['program_id']
#         year = kwargs['year']

#         try:
#             # Fetch or create the program
#             program = Program.objects.get(id=program_id)

#             # Fetch or create the timetable for the program and year
#             timetable, created = Timetable.objects.get_or_create(program=program, year=year)
#             self.stdout.write(f"Timetable created: {created}, ID: {timetable.id}")

#             # Fetch relevant data for scheduling
#             courses = Course.objects.filter(program=program, course_year=year)
#             timeslots = TimeSlot.objects.all()
#             rooms = Room.objects.all()
#             staff = Staff.objects.filter(role='Lecturer')

#             # Print data fetched
#             self.stdout.write(f"Courses: {courses}")
#             self.stdout.write(f"Timeslots: {timeslots}")
#             self.stdout.write(f"Rooms: {rooms}")
#             self.stdout.write(f"Staff: {staff}")

#             # Initialize variables to track occupied timeslots
#             room_occupied = {room.id: set() for room in rooms}
#             staff_occupied = {lecturer.id: set() for lecturer in staff}

#             # Generate CourseSchedule instances for the entire week
#             for course in courses:
#                 assigned_timeslots = []
#                 for day, _ in TimeSlot.DAY_CHOICES:
#                     for timeslot in timeslots.filter(day=day):
#                         if timeslot in assigned_timeslots:
#                             continue
#                         for room in rooms:
#                             if timeslot.id not in room_occupied[room.id]:
#                                 for lecturer in staff:
#                                     if timeslot.id not in staff_occupied[lecturer.id]:
#                                         # Create CourseSchedule instance
#                                         schedule = CourseSchedule(
#                                             timetable=timetable,
#                                             course=course,
#                                             room=room,
#                                             timeslot=timeslot,
#                                             staff=lecturer
#                                         )
#                                         try:
#                                             Print(schedule)
#                                             schedule.save()
#                                             room_occupied[room.id].add(timeslot.id)
#                                             staff_occupied[lecturer.id].add(timeslot.id)
#                                             assigned_timeslots.append(timeslot)
#                                             self.stdout.write(f"Assigned {course.course_name} to {room.room_name} at {timeslot.day} {timeslot.time_range} with {lecturer.username}")
#                                             break
#                                         except ValidationError as e:
#                                             self.stderr.write(f"Validation error: {e}")
#                                             continue
#                         if timeslot in assigned_timeslots:
#                             break
#                 if not assigned_timeslots:
#                     self.stderr.write(f"Could not assign course {course.course_name} due to conflicts.")

#             self.stdout.write(self.style.SUCCESS('Timetable generated successfully'))

#         except Program.DoesNotExist:
#             self.stderr.write(f"Program with ID {program_id} does not exist.")
#         except Exception as e:
#             self.stderr.write(f"An error occurred: {e}")

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
                                break
                            except ValidationError as e:
                                self.stdout.write(f"Could not assign {course.course_name} due to conflict: {str(e)}")
                        if assigned:
                            break
                    if assigned:
                        break
                if assigned:
                    break

            if not assigned:
                self.stdout.write(f"Could not assign course {course.course_name} due to conflicts.")
