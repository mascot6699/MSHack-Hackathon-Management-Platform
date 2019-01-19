# Django project configuration, if environ vars are missing
#
#   This is a sample file. Rename to local.env for a quick development
#   settings. Git will not track local.env as it contains confidential
#   information. So store a backup of this file outside this repo.
#
# Note: No spaces around '=' sign and no quotes for righthand values.

DEBUG=True
# syntax: DATABASE_URL=postgres://username:password@127.0.0.1:5432/database
DATABASE_URL=sqlite:///db.sqlite3
# Command to create a new secret key:
# $ python -c 'import random; import string; print("".join([random.SystemRandom().choice(string.digits + string.ascii_letters + string.punctuation) for i in range(100)]))'
SECRET_KEY=4)3zir^tuqs!bu&ifi8l2i(@yfjjnhv6&^ql%qtw@b==$k7y-+
