class Password(object):

    def __init__(self) -> None:
        self.password = None
        self.policy = None

    def isValid(self) -> bool:
        count = self.password.count(self.policy.char)
        return self.policy.max >= count >= self.policy.min


class Policy(object):
    pass


def parseString(password: str) -> Password:
    p = Password()
    policy = Policy()
    p.password = password.split(':')[1].strip()
    policy_str = password.split(':')[0]
    policy.min = int(policy_str.split('-')[0])
    policy.max = int(policy_str.split('-')[1].split()[0])
    policy.char = policy_str.split()[1]
    p.policy = policy
    return p
