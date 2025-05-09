
bulky = 1000000 # cm
max_dimention = 150 # cm
max_heavy = 20 # kg

def is_standard(package: dict) -> bool:
    if (package['width'] * package["height"] * package["length"]) < bulky and package['mass'] < max_heavy:
        return True
    else:
        return False

def is_special(package: dict) -> bool:
    if (package['width'] * package["height"] * package["length"]) >= bulky or package['mass'] >= max_heavy:
        return True
    else:
        return False

def is_rejected(package: dict) -> bool:
    if (package['width'] * package["height"] * package["length"]) >= bulky and package['mass'] >= max_heavy:
        return True
    else:
        return False


def sort(width: list, height: list, length: list, package: dict) -> None:
    if is_standard(package):
        width.append(package)
        print("Package is standard")
    elif is_special(package):
        height.append(package)
        print("Package is special")
    elif is_rejected(package):
        length.append(package)
        print("Package is rejected")
    else:   
        print("Package is not valid")

packages = [
    {"width": 10, "height": 20, "length": 30, "mass": 5},
    {"width": 50, "height": 60, "length": 70, "mass": 15},
    {"width": 200, "height": 300, "length": 400, "mass": 25},
    {"width": 150, "height": 150, "length": 150, "mass": 10},
    {"width": 1000, "height": 2000, "length": 3000, "mass": 500},
    {"width": 120, "height": 130, "length": 140, "mass": 18},
    {"width": 10, "height": 10, "length": 10, "mass": 1},
    {"width": 300, "height": 400, "length": 500, "mass": 30},
    {"width": 80, "height": 90, "length": 100, "mass": 12},
    {"width": 250, "height": 250, "length": 250, "mass": 22},
    {"width": 5, "height": 5, "length": 5, "mass": 0.5},
    {"width": 600, "height": 700, "length": 800, "mass": 100},
    {"width": 500, "height": 500, "length": 500, "mass": 50},  # Rejected package
]

def main():
    for package in packages:
        print("=====================================")
        print(f"Processing package: {package}")
        bulky_packages = []
        special_packages = []
        rejected_packages = []
        sort(bulky_packages, special_packages, rejected_packages, package)

if __name__ == "__main__":
    main()
