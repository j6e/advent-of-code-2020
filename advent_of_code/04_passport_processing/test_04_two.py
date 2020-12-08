import two

def test_byr_valid():
    for i in range(1920, 2003, 1):
        line = f"byr:{i} "
        assert two.validate_byr(line)
    
def test_byr_invalid():
    for i in range(1800, 1920, 1):
        line = f"byr:{i} "
        assert not two.validate_byr(line)

    for i in range(2003, 2030, 1):
        line = f"byr:{i} "
        assert not two.validate_byr(line)

def test_iyr_valid():
    for i in range(2010, 2021, 1):
        line = f"iyr:{i} "
        assert two.validate_iyr(line)

def test_iyr_invalid():
    for i in range(1900, 2010, 1):
        line = f"iyr:{i} "
        assert not two.validate_iyr(line)

    for i in range(2021, 2050, 1):
        line = f"iyr:{i} "
        assert not two.validate_iyr(line)

def test_eyr_valid():
    for i in range(2020, 2031, 1):
        line = f"eyr:{i} "
        assert two.validate_eyr(line)

def test_eyr_invalid():
    for i in range(1900, 2020, 1):
        line = f"eyr:{i} "
        assert not two.validate_eyr(line)

    for i in range(2031, 2100, 1):
        line = f"eyr:{i} "
        assert not two.validate_eyr(line)

def test_hgt_cm_valid():
    for i in range(150, 194, 1):
        line = f"hgt:{i}cm "
        assert two.validate_hgt(line)

def test_hgt_in_valid():
    for i in range(59, 77, 1):
        line = f"hgt:{i}in "
        assert two.validate_hgt(line)

def test_hgt_cm_invalid():
    assert not two.validate_hgt(f"hgt:Acmsawd1 ")
    for i in range(0, 150, 1):
        line = f"hgt:{i}cm "
        assert not two.validate_hgt(line)
    for i in range(194, 300, 1):
        line = f"hgt:{i}cm "
        assert not two.validate_hgt(line)

def test_hgt_in_invalid():
    assert not two.validate_hgt(f"hgt:Ainsawd1 ")
    for i in range(0, 59, 1):
        line = f"hgt:{i}in "
        assert not two.validate_hgt(line)
    for i in range(77, 300, 1):
        line = f"hgt:{i}in "
        assert not two.validate_hgt(line)

def test_hcl_valid():
    assert two.validate_hcl("hcl:#123456 ")
    assert two.validate_hcl("hcl:#123abc ")
    assert two.validate_hcl("hcl:#abcdef ")
    assert two.validate_hcl("hcl:#012345 ")

def test_hcl_invalid():
    assert not two.validate_hcl("hcl:123456 ")
    assert not two.validate_hcl("hcl:123abc ")
    assert not two.validate_hcl("hcl:#abcdef1 ")
    assert not two.validate_hcl("hcl:#0123456 ")
    assert not two.validate_hcl("hcl:#ABCDEF ")