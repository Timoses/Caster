from json_serializer.Serializer import Serializer


class ClientAction(object):

    """Docstring for ClientAction. """

    def __init__(self, action):
        """TODO: to be defined. """

        import orjson
        import json
        sr = orjson.dumps(action.__dict__)

        self._action = action
        print(action.__dict__)
        self._original_execute = self._action.execute
        self._action.execute = self._execute
        action._name = 'tse'


    def create(action):
        print('hsaldfjlasdjf')
        print(action)

        print(action.execute)
        ClientAction(action)
        print(action.execute)
        #action.execute = client_action._execute

        return action
        #print(action.__dict__)
#        import json
#        self.print(json.dumps(action.__dict__))

    create = staticmethod(create)

    def _execute(self, *args, **kwargs):
        print('sdfsdfsdfsf')
        print(args)
        print(type(args))
        print(type(*args))
        self._original_execute(*args)
