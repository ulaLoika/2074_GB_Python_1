import os

def show_stats(base_dir):
    thresholds = {10 ** x: 0 for x in range (1, 6)}
    thresholds[0] = 0

    for root, dirs, files in os.walk(base_dir):
        if files:
            for file in files:
                size = os.stat(os.path.join(root, file)).st_size
                for key in sorted(thresholds.keys()):
                    if size > key:
                        continue
                    else:
                        thresholds[key]+=1
                        break

    return {threshold:count for (threshold, count) in sorted(thresholds.items())}


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath('some_data'))
    print (show_stats(base_dir))
