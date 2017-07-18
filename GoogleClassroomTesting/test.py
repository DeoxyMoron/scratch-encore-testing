import quickstart


def getCourseList():
    service = quickstart.getService()
    results = service.courses().list(pageSize=10).execute()
    courses = results.get('courses', [])

    if not courses:
        print('No courses found.')
    else:
        print('Courses:')
        for course in courses:
            print(course['name'])

    return courses


courseList = getCourseList()

# Get an ID for a course
course2id = courseList[0]["id"]
print(course2id)

# Sample course data
courseWork = {
    'title': 'Ant colonies',
    'description': 'Read the ar and complete the quiz.',
    'materials': [
        {'link': {'url': 'http://example.com/ant-colonies'}},
        {'link': {'url': 'http://example.com/ant-quiz'}}
    ],
    'workType': 'ASSIGNMENT',
    'state': 'PUBLISHED',
}

# Create a course
service = quickstart.getService()
courseWork = service.courses().courseWork().create(
    courseId='6965808975', body=courseWork).execute()
print('Assignment created with ID {0}'.format(courseWork.get('id')))
