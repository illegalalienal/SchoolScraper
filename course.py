class Course:
    def __init__(self, CRN, Course, Section, Credits, Title, Notes, Days, Times, Place, Instructor, Cap):
        self.CRN = CRN
        self.Course = Course
        self.Section = Section
        self.Credits = Credits
        self.Title = Title
        self.Notes = Notes
        self.Days = Days
        self.Times = Times
        self.Place = Place
        self.Instructor = Instructor
        self.Cap = Cap

    def __str__(self):
        return f"{self.Title} with {self.Instructor}, Section {self.Section}"