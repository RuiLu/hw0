import string;
count = 0;
template = 'single malt scotch';
with open("iowa-liquor-sample.csv") as f:
	for line in f:
		temp = line.lower();
		if (string.find(temp, template) != -1):
			count += 1;
print 'The result is:', count;
