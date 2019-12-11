def prop_GAC(csp, newVar=None):
# GAC = General Arc Consistency
    '''Do GAC propagation. If newVar is None we do initial GAC enforce 
       processing all constraints. Otherwise we do GAC enforce with
       constraints containing newVar on GAC Queue'''
#IMPLEMENT
    
    queue = []
    pruned = []
    cons = csp.get_all_cons()

    if not newVar:
        queue = cons.copy()
    else:
        queue = csp.get_cons_with_var(newVar).copy()

    # For looping queue use an indicator count. It avoids keep append and
    # remove items in the queue list that may slow down the program.
    count = 0
    while count < len(queue):
        
        con = queue[count]       
        scope = con.get_scope()

        for i in range(len(scope)):
            var = scope[i]
            curdom = var.cur_domain()
            found = False
            for val in curdom:
                if con.has_support(var, val):
                    continue
                else:
                    found = True
                    var.prune_value(val)
                    pruned.append((var, val))
                    if not var.cur_domain_size():
                        queue = []
                        return (False, pruned)

            if found:
                cons = csp.get_cons_with_var(var)
                for c in cons:
                    if c not in queue[count:]:
                        queue.append(c)
        count += 1

    return (True, pruned)