# # # from django.core.management.base import BaseCommand
# # # from django.core.exceptions import ValidationError
# # # from store.models import Course, Room, TimeSlot, Staff, Timetable, CourseSchedule, Program

# # # class Command(BaseCommand):
# # #     help = 'Auto-generate timetable for a given program and year'

# # #     def add_arguments(self, parser):
# # #         parser.add_argument('program_id', type=int, help='The ID of the program')
# # #         parser.add_argument('year', type=int, help='The year of the program')

# # #     def handle(self, *args, **kwargs):
# # #         program_id = kwargs['program_id']
# # #         year = kwargs['year']

# # #         try:
# # #             # Fetch data
# # #             program = Program.objects.get(id=program_id)
# # #             courses = Course.objects.filter(program=program, course_year=year)
# # #             timeslots = TimeSlot.objects.all()
# # #             rooms = Room.objects.all()
# # #             staff = Staff.objects.filter(role='Lecturer')

# # #             # Initialize timetable
# # #             timetable, created = Timetable.objects.get_or_create(program=program, year=year)

# # #             # Initialize variables to keep track of occupied timeslots
# # #             room_occupied = {room.id: set() for room in rooms}
# # #             staff_occupied = {lecturer.id: set() for lecturer in staff}

# # #             for course in courses:
# # #                 assigned = False
# # #                 for timeslot in timeslots:
# # #                     if assigned:
# # #                         break
# # #                     for room in rooms:
# # #                         if timeslot.id not in room_occupied[room.id]:
# # #                             for lecturer in staff:
# # #                                 if timeslot.id not in staff_occupied[lecturer.id]:
# # #                                     # Assign course
# # #                                     schedule = CourseSchedule(
# # #                                         timetable=timetable,
# # #                                         course=course,
# # #                                         room=room,
# # #                                         timeslot=timeslot,
# # #                                         staff=lecturer
# # #                                     )
# # #                                     try:
# # #                                         schedule.save()
# # #                                         room_occupied[room.id].add(timeslot.id)
# # #                                         staff_occupied[lecturer.id].add(timeslot.id)
# # #                                         assigned = True
# # #                                         break
# # #                                     except ValidationError as e:
# # #                                         self.stderr.write(f"Validation error: {e}")
# # #                                         continue
# # #                 if not assigned:
# # #                     self.stderr.write(f"Could not assign course {course.course_name} due to conflicts.")

# # #             self.stdout.write(self.style.SUCCESS('Timetable generated successfully'))

# # #         except Program.DoesNotExist:
# # #             self.stderr.write(f"Program with ID {program_id} does not exist.")
# # #         except Exception as e:
# # #             self.stderr.write(f"An error occurred: {e}")


# # # generate_timetable.py

# # from django.core.management.base import BaseCommand
# # from django.core.exceptions import ValidationError
# # from store.models import Course, Room, TimeSlot, Staff, Timetable, CourseSchedule, Program

# # class Command(BaseCommand):
# #     help = 'Auto-generate timetable for a given program and year'

# #     def add_arguments(self, parser):
# #         parser.add_argument('program_id', type=int, help='The ID of the program')
# #         parser.add_argument('year', type=int, help='The year of the program')

# #     def handle(self, *args, **kwargs):
# #         program_id = kwargs['program_id']
# #         year = kwargs['year']

# #         # Fetch data
# #         program = Program.objects.get(id=program_id)
# #         courses = Course.objects.filter(program_id=program_id, course_year=year)
# #         timeslots = TimeSlot.objects.all()
# #         rooms = Room.objects.all()
# #         staff = Staff.objects.filter(role='Lecturer')

# #         # Initialize timetable
# #         timetable, created = Timetable.objects.get_or_create(program_id=program_id, year=year)

# #         # Initialize variables to keep track of occupied timeslots
# #         room_occupied = {room.id: {timeslot.id: None for timeslot in timeslots} for room in rooms}
# #         staff_occupied = {lecturer.id: {timeslot.id: None for timeslot in timeslots} for lecturer in staff}

# #         # Loop through each day of the week and each timeslot
# #         for day, _ in TimeSlot.DAY_CHOICES:
# #             for timeslot in timeslots:
# #                 for course in courses:
# #                     assigned = False
# #                     for room in rooms:
# #                         if assigned:
# #                             break
# #                         if not room_occupied[room.id][timeslot.id]:
# #                             for lecturer in staff:
# #                                 if not staff_occupied[lecturer.id][timeslot.id]:
# #                                     # Assign course
# #                                     schedule = CourseSchedule(
# #                                         timetable=timetable,
# #                                         course=course,
# #                                         room=room,
# #                                         timeslot=timeslot,
# #                                         staff=lecturer
# #                                     )
# #                                     try:
# #                                         schedule.save()
# #                                         room_occupied[room.id][timeslot.id] = course
# #                                         staff_occupied[lecturer.id][timeslot.id] = course
# #                                         assigned = True
# #                                         break
# #                                     except ValidationError as e:
# #                                         self.stderr.write(f"Validation error: {e}")
# #                                         continue
# #                     if not assigned:
# #                         self.stderr.write(f"Could not assign course {course.course_name} on {day} at {timeslot.time_range} due to conflicts.")

# #         self.stdout.write(self.style.SUCCESS('Timetable generated successfully'))


# # from django.core.management.base import BaseCommand
# # from django.core.exceptions import ValidationError
# # from store.models import Course, Room, TimeSlot, Staff, Timetable, CourseSchedule, Program

# # class Command(BaseCommand):
# #     help = 'Auto-generate timetable for a given program and year'

# #     def add_arguments(self, parser):
# #         parser.add_argument('program_id', type=int, help='The ID of the program')
# #         parser.add_argument('year', type=int, help='The year of the program')

# #     def handle(self, *args, **kwargs):
# #         program_id = kwargs['program_id']
# #         year = kwargs['year']

# #         try:
# #             # Fetch data
# #             program = Program.objects.get(id=program_id)
# #             courses = Course.objects.filter(program=program, course_year=year)
# #             timeslots = TimeSlot.objects.all()
# #             rooms = Room.objects.all()
# #             staff = Staff.objects.filter(role='Lecturer')

# #             # Initialize timetable
# #             timetable, created = Timetable.objects.get_or_create(program_id=program_id, year=year)

# #             # Initialize variables to keep track of occupied timeslots
# #             room_occupied = {room.id: set() for room in rooms}
# #             staff_occupied = {lecturer.id: set() for lecturer in staff}

# #             # Loop through each course and try to assign it to a timeslot, room, and lecturer
# #             for course in courses:
# #                 assigned = False
# #                 for timeslot in timeslots:
# #                     if assigned:
# #                         break
# #                     for room in rooms:
# #                         if timeslot.id not in room_occupied[room.id]:
# #                             for lecturer in staff:
# #                                 if timeslot.id not in staff_occupied[lecturer.id]:
# #                                     # Assign course
# #                                     schedule = CourseSchedule(
# #                                         timetable=timetable,
# #                                         course=course,
# #                                         room=room,
# #                                         timeslot=timeslot,
# #                                         staff=lecturer
# #                                     )
# #                                     try:
# #                                         schedule.save()
# #                                         room_occupied[room.id].add(timeslot.id)
# #                                         staff_occupied[lecturer.id].add(timeslot.id)
# #                                         assigned = True
# #                                         break
# #                                     except ValidationError as e:
# #                                         self.stderr.write(f"Validation error: {e}")
# #                                         continue
# #                 if not assigned:
# #                     self.stderr.write(f"Could not assign course {course.course_name} due to conflicts.")

# #             self.stdout.write(self.style.SUCCESS('Timetable generated successfully'))

# #         except Program.DoesNotExist:
# #             self.stderr.write(f"Program with ID {program_id} does not exist.")
# #         except Exception as e:
# #             self.stderr.write(f"An error occurred: {e}")


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
#             # Fetch data
#             program = Program.objects.get(id=program_id)
#             courses = Course.objects.filter(program=program, course_year=year)
#             timeslots = TimeSlot.objects.all()
#             rooms = Room.objects.all()
#             staff = Staff.objects.filter(role='Lecturer')

#             # Initialize timetable
#             timetable, created = Timetable.objects.get_or_create(program_id=program_id, year=year)

#             # Initialize variables to keep track of occupied timeslots
#             room_occupied = {room.id: set() for room in rooms}
#             staff_occupied = {lecturer.id: set() for lecturer in staff}

#             # Loop through each course and try to assign it to a timeslot, room, and lecturer
#             for course in courses:
#                 assigned = False
#                 for timeslot in timeslots:
#                     if assigned:
#                         break
#                     for room in rooms:
#                         if timeslot.id not in room_occupied[room.id]:
#                             for lecturer in staff:
#                                 if timeslot.id not in staff_occupied[lecturer.id]:
#                                     # Assign course
#                                     schedule = CourseSchedule(
#                                         timetable=timetable,
#                                         course=course,
#                                         room=room,
#                                         timeslot=timeslot,
#                                         staff=lecturer
#                                     )
#                                     try:
#                                         schedule.full_clean()  # Validate the model manually
#                                         schedule.save()
#                                         print("CourseSchedule saved successfully!")
#                                         room_occupied[room.id].add(timeslot.id)
#                                         staff_occupied[lecturer.id].add(timeslot.id)
#                                         assigned = True
#                                         break
#                                     except ValidationError as e:
#                                         print(f"Validation error: {e}")
#                                         self.stderr.write(f"Validation error: {e}")
#                                         continue
#                 if not assigned:
#                     self.stderr.write(f"Could not assign course {course.course_name} due to conflicts.")

#             self.stdout.write(self.style.SUCCESS('Timetable generated successfully'))

#         except Program.DoesNotExist:
#             self.stderr.write(f"Program with ID {program_id} does not exist.")
#         except Exception as e:
#             self.stderr.write(f"An error occurred: {e}")


from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from store.models import Course, Room, TimeSlot, Staff, Timetable, CourseSchedule, Program

class Command(BaseCommand):
    help = 'Auto-generate timetable for a given program and year'

    def add_arguments(self, parser):
        parser.add_argument('program_id', type=int, help='The ID of the program')
        parser.add_argument('year', type=int, help='The year of the program')

    def handle(self, *args, **kwargs):
        program_id = kwargs['program_id']
        year = kwargs['year']

        try:
            # Fetch or create the program
            program = Program.objects.get(id=program_id)

            # Fetch or create the timetable for the program and year
            timetable, created = Timetable.objects.get_or_create(program=program, year=year)
            self.stdout.write(f"Timetable created: {created}, ID: {timetable.id}")

            # Fetch relevant data for scheduling
            courses = Course.objects.filter(program=program, course_year=year)
            timeslots = TimeSlot.objects.all()
            rooms = Room.objects.all()
            staff = Staff.objects.filter(role='Lecturer')

            # Print data fetched
            self.stdout.write(f"Courses: {courses}")
            self.stdout.write(f"Timeslots: {timeslots}")
            self.stdout.write(f"Rooms: {rooms}")
            self.stdout.write(f"Staff: {staff}")

            # Initialize variables to track occupied timeslots
            room_occupied = {room.id: set() for room in rooms}
            staff_occupied = {lecturer.id: set() for lecturer in staff}

            # Generate CourseSchedule instances for the entire week
            for course in courses:
                assigned_timeslots = []
                for day, _ in TimeSlot.DAY_CHOICES:
                    for timeslot in timeslots.filter(day=day):
                        if timeslot in assigned_timeslots:
                            continue
                        for room in rooms:
                            if timeslot.id not in room_occupied[room.id]:
                                for lecturer in staff:
                                    if timeslot.id not in staff_occupied[lecturer.id]:
                                        # Create CourseSchedule instance
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
                                            assigned_timeslots.append(timeslot)
                                            self.stdout.write(f"Assigned {course.course_name} to {room.room_name} at {timeslot.day} {timeslot.time_range} with {lecturer.username}")
                                            break
                                        except ValidationError as e:
                                            self.stderr.write(f"Validation error: {e}")
                                            continue
                        if timeslot in assigned_timeslots:
                            break
                if not assigned_timeslots:
                    self.stderr.write(f"Could not assign course {course.course_name} due to conflicts.")

            self.stdout.write(self.style.SUCCESS('Timetable generated successfully'))

        except Program.DoesNotExist:
            self.stderr.write(f"Program with ID {program_id} does not exist.")
        except Exception as e:
            self.stderr.write(f"An error occurred: {e}")
