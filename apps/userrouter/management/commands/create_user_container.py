from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = '<username>'
    help = 'Creates a container for the given user if it doesn\'t exist'

    def handle(self, *args, **options):
        from userrouter.tasks import create_user_container
        import cloudfiles
        from cloudfiles.errors import NoSuchContainer
        from cumulus import settings

        for username in args:
            
            container_name = username
            conn = cloudfiles.get_connection(
                            username=settings.CUMULUS['USERNAME'],
                            api_key=settings.CUMULUS['API_KEY'])

            try:
                container = conn.get_container(container_name)
                self.stdout.write(f"Container for {username} already exists.")
            except NoSuchContainer:
                container = conn.create_container(container_name)
                container.make_public()
                self.stdout.write(f"Successfully created container for {username}.")
