def perimeter(cows, connections):
    groups = [] # list of sets of cows

    for connection in connections:
        for group in groups:
            # if any of the cows in the connection are in the group
            if connection[0] in group or connection[1] in group:
                # add the other cow to the group
                group.add(connection[0])
                group.add(connection[1])
                break
        else:
            # if no group was found, create a new group
            groups.append(set(connection))

        # merge the groups that share a cow
        for group in groups:
            for other_group in groups:
                if group is not other_group and group & other_group:
                    group |= other_group
                    groups.remove(other_group)
                    break

    # any cow that is not a member of a group is in its own group
    for cow_ind in range(1, len(cows) +1):
        if not any(cow_ind in group for group in groups):
            groups.append(set(cow_ind))

    # calculate the perimeter of each group
    group_perimeters = []
    for group in groups:
        group_cows = [cows[cow_ind - 1] for cow_ind in group]
        # max x - min x
        x_range = max(cow[0] for cow in group_cows) - min(cow[0] for cow in group_cows)
        # max y - min y
        y_range = max(cow[1] for cow in group_cows) - min(cow[1] for cow in group_cows)
        group_perimeters.append(2 * (x_range + y_range))

    return min(group_perimeters)

