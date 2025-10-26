class UpdateManager:
    updatables = []

    @classmethod
    def add_updatable(cls, updatable):
        if updatable in cls.updatables:
            return
        cls.updatables.append(updatable)

    @classmethod
    def remove_updatable(cls, updatable):
        if updatable not in cls.updatables:
            return
        cls.updatables.remove(updatable)

    @classmethod
    def clear_updatables(cls):
        cls.updatables.clear()

    @classmethod
    def update(cls):
        for updatable in cls.updatables:
            if not updatable.is_active():
                continue
            updatable.update()

class DrawManager:
    drawables = []

    @classmethod
    def add_drawable(cls, drawable):
        if drawable in cls.drawables:
            return
        cls.drawables.append(drawable)

    @classmethod
    def remove_drawable(cls, drawable):
        if drawable not in cls.drawables:
            return
        cls.drawables.remove(drawable)

    @classmethod
    def clear_drawables(cls):
        cls.drawables.clear()

    @classmethod
    def draw(cls):
        for drawable in cls.drawables:
            if not drawable.is_active():
                continue
            drawable.draw()

class CollisionManager:
    collidables = []

    @classmethod
    def add_collidable(cls, collidable):
        if collidable in cls.collidables:
            return
        cls.collidables.append(collidable)

    @classmethod
    def remove_collidable(cls, collidable):
        if collidable not in cls.collidables:
            return
        cls.collidables.remove(collidable)

    @classmethod
    def clear_collidables(cls):
        cls.collidables.clear()

    @classmethod
    def check_collisions(cls):
        for i in range(len(cls.collidables) - 1):
            for j in range(i + 1, len(cls.collidables)):
                if not cls.collidables[i].is_active() or not cls.collidables[j].is_active():
                    continue
                check1 = cls.collidables[i].can_collide_with(cls.collidables[j])
                check2 = cls.collidables[j].can_collide_with(cls.collidables[i])
                if (check1 or check2) and cls.collidables[i].does_collide(cls.collidables[j]):
                    if check1:
                        cls.collidables[i].on_collision(cls.collidables[j])
                    if check2:
                        cls.collidables[j].on_collision(cls.collidables[i])

class ScoreManager:
    scores = []

    @classmethod
    def register_player(cls, player_id):
        for score in cls.scores:
            if score["player_id"] == player_id:
                return
        cls.scores.append({"player_id" : player_id, "score" : 0})

    @classmethod
    def update_score(cls, player_id, value = 1):
        for score in cls.scores:
            if score["player_id"] == player_id:
                score.update({"score" : score["score"] + value})

    @classmethod
    def get_score(cls, player_id):
        for score in cls.scores:
            if score["player_id"] == player_id:
                return score["score"]

    @classmethod
    def get_scores(cls):
        return cls.scores

class EventManager:
    subscribers = {}

    @classmethod
    def subscribe(cls, event_name, subscriber):
        if event_name not in cls.subscribers:
            cls.subscribers[event_name] = []
        if subscriber not in cls.subscribers[event_name]:
            cls.subscribers[event_name].append(subscriber)

    @classmethod
    def unsubscribe(cls, event_name, subscriber):
        if event_name not in cls.subscribers:
            return
        cls.subscribers[event_name].remove(subscriber)

    @classmethod
    def publish(cls, event_name, **kwargs):
        for subscriber in cls.subscribers.get(event_name, []):
            subscriber(**kwargs)
