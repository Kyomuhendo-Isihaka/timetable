import random
from store.models import Timetable, Course, Room, TimeSlot, Staff, CourseSchedule,Program
from django.core.exceptions import ValidationError


def generate_timetable(program_id, year):
    timetable = Timetable.objects.create(program_id=program_id, year=year)
    courses = Course.objects.filter(program_id=program_id, course_year=year)
    timeslots = TimeSlot.objects.all()
    rooms = Room.objects.all()
    staff_members = Staff.objects.filter(role='Lecturer')

    for course in courses:
        timeslot = random.choice(timeslots)
        room = random.choice(rooms)
        staff = random.choice(staff_members)

        schedule = CourseSchedule(
            timetable=timetable,
            course=course,
            room=room,
            timeslot=timeslot,
            staff=staff
        )

        try:
            schedule.save()
            print(f'Successfully scheduled {course.course_name}')
        except ValidationError as e:
            print(f'Error scheduling {course.course_name}: {e}')




def handle(self, *args, **options):
    programs = Program.objects.all()
    timeslots = TimeSlot.objects.all()
    rooms = Room.objects.all()
    staff_members = Staff.objects.filter(role='Lecturer')

    for program in programs:
        for year in range(1, 5):  # Assuming 4 years of study
            timetable = Timetable.objects.create(program=program, year=year)
            courses = Course.objects.filter(program=program, course_year=year)

            for course in courses:
                timeslot = random.choice(timeslots)
                room = random.choice(rooms)
                staff = random.choice(staff_members)

                schedule = CourseSchedule(
                    timetable=timetable,
                    course=course,
                    room=room,
                    timeslot=timeslot,
                    staff=staff
                )

                try:
                    schedule.save()
                    self.stdout.write(self.style.SUCCESS(f'Successfully scheduled {course.course_name}'))
                except ValidationError as e:
                    self.stdout.write(self.style.ERROR(f'Error scheduling {course.course_name}: {e}'))

