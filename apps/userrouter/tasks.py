from celery.task import task

@task
def create_user_container(user):
    """
    Create a container for a user (probably a new user)
    """
    import cloudfiles
    from cloudfiles.errors import NoSuchContainer
    from cumulus import settings
    
    container_name = user.username
    conn = cloudfiles.get_connection(
                    username=settings.CUMULUS['USERNAME'],
                    api_key=settings.CUMULUS['API_KEY'])
    
    try:
        container = conn.get_container(container_name)
    except NoSuchContainer:
        container = conn.create_container(container_name)
        container.make_public()
