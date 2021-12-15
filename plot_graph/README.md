# A Simple RESTful API with Flask
shows the beginnings of a very simple Flask-based RESTful server. This only implements HTTP GET requests for consuming data.

# Using Static or Dynamic Delivery?
When to use static or dynamic delivery is highly dependent on context
and is an inevitable compromise. Bandwidths vary regionally and with devices.
For example, if you’re developing a visualization that should be accessible
from a smartphone in a rural context, the data constraints are very different
from those of an in-house data app running on a local network.


The ultimate guide is user experience. If a little wait at the beginning while the data
caches leads to a lightning-fast JavaScript dataviz, then purely static delivery may well
be the answer. If you are allowing the user to cut and slice a large, multivariate dataset,
then this probably won’t be possible without an annoyingly long wait time. As a rough rule
of thumb, any dataset less than 200 KB should be finewith purely static delivery. As you move
into the megabytes of data and beyond, you’ll probably need a database-driven API from which
to fetch your data.
