import requests


class Catalog():
    def __init__(self):
        self.options = {
            'url': 'https://www.udacity.com/public-api/v0/courses \
                    ?projection=internal'
        }

    def __get(self):
        catalog = None  # need to find or make caching library

        if catalog:
            return catalog
        else:
            req = requests.get(self.options['url'])

            if req.status_code == 404:
                raise Exception('404 page not found')
            elif req.status_code == 500:
                raise Exception('500 server error')
            else:
                # put in cache
                return req.json()

    def catalog(self):
        try:
            data = self.__get()
            return data
        except:
            return None

    def courses(self):
        try:
            data = self.__get()
            return data.get('courses')
        except:
            return None

    def course(self, key):
        try:
            data = self.__get()
            if 'courses' in data:
                courses_generator = (course for course in data['courses'])
                for course in courses_generator:
                    if course['key'] == key:
                        return course
        except:
            return None

    def instructors(self, key):
        try:
            data = self.course(key)
            return data.get('instructors')
        except:
            return None

if __name__ == '__main__':
    cat = Catalog()
    x = cat.catalog()
    print(x['tracks'])


    c = cat.courses()
    print(c[0]['key'])

    d = cat.course('cs191')
    print(d)

    d = cat.course('cs101')
    print(d)

    e = cat.instructors('cs11')
    print(e)
