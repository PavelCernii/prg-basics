class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(f'Timeline of {self.username}:')
        index = 1
        for post in self.posts:
            print(f'{index}.{post}')
            index += 1


johndoe = SocialMediaProfile('johndoe')

johndoe.add_post('111')
johndoe.add_post('222')
johndoe.add_post('333')

johndoe.display_timeline()
