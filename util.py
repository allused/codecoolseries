from data import queries


def shows_sum():
    actors = queries.get_actors()
    top_ten_actor = []
    for i in range(10):
        top_ten_actor.append(actors[i]['cnt'])
    return sum(top_ten_actor)



