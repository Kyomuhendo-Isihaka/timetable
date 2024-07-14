# import random
# from store.models import Timetable, Course, Room, TimeSlot, Staff, CourseSchedule,Program
# from django.core.exceptions import ValidationError


# def generate_timetable(program_id, year):
#     timetable = Timetable.objects.create(program_id=program_id, year=year)
#     courses = Course.objects.filter(program_id=program_id, course_year=year)
#     timeslots = TimeSlot.objects.all()
#     rooms = Room.objects.all()
#     staff_members = Staff.objects.filter(role='Lecturer')

#     for course in courses:
#         timeslot = random.choice(timeslots)
#         room = random.choice(rooms)
#         staff = random.choice(staff_members)

#         schedule = CourseSchedule(
#             timetable=timetable,
#             course=course,
#             room=room,
#             timeslot=timeslot,
#             staff=staff
#         )

#         try:
#             schedule.save()
#             print(f'Successfully scheduled {course.course_name}')
#         except ValidationError as e:
#             print(f'Error scheduling {course.course_name}: {e}')




# def handle(self, *args, **options):
#     programs = Program.objects.all()
#     timeslots = TimeSlot.objects.all()
#     rooms = Room.objects.all()
#     staff_members = Staff.objects.filter(role='Lecturer')

#     for program in programs:
#         for year in range(1, 5):  # Assuming 4 years of study
#             timetable = Timetable.objects.create(program=program, year=year)
#             courses = Course.objects.filter(program=program, course_year=year)

#             for course in courses:
#                 timeslot = random.choice(timeslots)
#                 room = random.choice(rooms)
#                 staff = random.choice(staff_members)

#                 schedule = CourseSchedule(
#                     timetable=timetable,
#                     course=course,
#                     room=room,
#                     timeslot=timeslot,
#                     staff=staff
#                 )

#                 try:
#                     schedule.save()
#                     self.stdout.write(self.style.SUCCESS(f'Successfully scheduled {course.course_name}'))
#                 except ValidationError as e:
#                     self.stdout.write(self.style.ERROR(f'Error scheduling {course.course_name}: {e}'))


# management/commands/generate_timetable.py

from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from store.models import Course, Room, TimeSlot, Staff, Timetable, CourseSchedule

class Command(BaseCommand):
    help = 'Auto-generate timetable for a given program and year'

    def add_arguments(self, parser):
        parser.add_argument('program_id', type=int, help='The ID of the program')
        parser.add_argument('year', type=int, help='The year of the program')

    def handle(self, *args, **kwargs):
        program_id = kwargs['program_id']
        year = kwargs['year']

        # Fetch data
        courses = Course.objects.filter(program_id=program_id, course_year=year)
        timeslots = TimeSlot.objects.all()
        rooms = Room.objects.all()
        staff = Staff.objects.filter(role='Lecturer')

        # Initialize timetable
        timetable, created = Timetable.objects.get_or_create(program_id=program_id, year=year)

        # Initialize variables to keep track of occupied timeslots
        room_occupied = {room.id: set() for room in rooms}
        staff_occupied = {lecturer.id: set() for lecturer in staff}

        for course in courses:
            assigned = False
            for timeslot in timeslots:
                if assigned:
                    break
                for room in rooms:
                    if timeslot.id not in room_occupied[room.id]:
                        for lecturer in staff:
                            if timeslot.id not in staff_occupied[lecturer.id]:
                                # Assign course
                                schedule = CourseSchedule(
                                    timetable=timetable,
                                    course=course,
                                    room=room,
                                    timeslot=timeslot,
                                    staff=lecturer
                                )
                                try:
                                    schedule.save()
                                    room_occupied[room.id].add(timeslot.id)
                                    staff_occupied[lecturer.id].add(timeslot.id)
                                    assigned = True
                                    break
                                except ValidationError as e:
                                    self.stderr.write(f"Validation error: {e}")
                                    continue
            if not assigned:
                self.stderr.write(f"Could not assign course {course.course_name} due to conflicts.")

        self.stdout.write(self.style.SUCCESS('Timetable generated successfully'))

