# Why Data Mining?
We live in a world where vast amounts of data are collected daily. Analyzing
such data is an important need. today we looks at how data mining can meet
this need by providing tools to discover knowledge from data and
we observe how data mining can be viewed as a result of the natural evolution
of information technology.

# Moving Towards the Information Age
“We are living in the information age” is a popular saying, however we are
actually living in the data age. Tera- or peta-bytes of data pour into our
computer networks, the World Wide Web (WWW), and various data storage
devices every day from business, science and engineering, medicine, and almost
every other aspect of our daily life. This explosive growth of available data
volume is a result of the computerization of our society and the fast development
of powerful data collection and storage tools. Businesses worldwide generate
gigantic data sets, including sales transactions, stock trading records, product
descriptions, sales promotions, company profiles and performance, and customer
feedback. 

For example, large stores like D-Mart handle hundreds of millions of
transactions per week at thousands of branches around the India. 

Scientific and engineering practices generate high-orders of peta-bytes of data in a continuous manner, from remote sensing, process measuring, scientific experiments, system
performance, engineering observations, and environment surveillance. 

Global backbone telecommunication networks carry tens of petabyes of data traffic
every day. 
The medical and health industry generates tremendous amounts of
data from medical records, patient monitoring, and medical images. 
Billions of Web searches supported by Web search engines process tens of petabytes
of data every day. 
Communities and social media have become increasingly
important data sources, producing digital pictures and videos, Web blogs,
Web communities, and various kinds of social networks. 
The list of sources generating huge amounts of data is endless.

# Example 1.1 Data mining turns a large collection of data into knowledge. 
A Web search engine like Google receives hundreds of millions of queries every day.
Each query can be viewed as a transaction where the user describes her/his
information need. 
What novel and useful knowledge can a Web search engine
learn from such a huge collection of search queries collected from users over
time? Interestingly, some patterns found in user search queries can disclose in-
valuable knowledge that cannot be obtained by reading individual data items
alone. 
For example, Google Flu Trends uses specific search terms as indicators
of flu activity. It found a close relationship between the number of people who
search for flu-related information and the number of people who actually have
flu symptoms. A pattern emerges when all of the search queries related to flu
are aggregated. 
Using aggregated Google search data, Google Flu Trends can
estimate flu activity up to two weeks faster than traditional systems2. This ex-
ample shows how data mining can turn a large collection of data into knowledge
that can help meet a global challenge of our times.

# **What is Data Mining?**  
Data Mining is the process of discovering interesting patterns, correlations, and knowledge from large amounts of data using statistical, machine learning, and database techniques.  
It is also known as **Knowledge Discovery in Databases (KDD)**.

# Data mining as a step in the process of knowledge discovery.
1. Data cleaning (to remove noise and inconsistent data)
2. Data integration (where multiple data sources may be combined)
3. Data selection (where data relevant to the analysis task are retrieved
from the database)
4. Data transformation (where data are transformed and consolidated into
forms appropriate for mining by performing summary or aggregation op-
erations)
5. Data mining (an essential process where intelligent methods are applied
in order to extract data patterns)
6. Pattern evaluation (to identify the truly interesting patterns represent-
ing knowledge based on interestingness measures)
7. Knowledge presentation (where visualization and knowledge represen-
tation techniques are used to present the mined knowledge to the user)

# What Kinds of Data Can Be Mined?
As a general technology, data mining can be applied to any kind of data as long as
the data are meaningful for a target application. 
The most basic forms of data for mining applications are database data , data warehouse data , and transactional data . 
Data mining can also be applied to other forms of data, such as data streams, ordered/sequence data, graph or networked data, spatial data, text data, multimedia data, and
the World Wide Web. 
Data mining will certainly continue to embrace new data types as they
emerge

## Database Data
A database system, also called a database management system (DBMS
for short), consists of a collection of interrelated data, known as a database,
and a set of software programs to manage and access the data. 

A relational database is a collection of tables, each of which is assigned a
unique name. Each table consists of a set of attributes (columns or fields) and
usually stores a large set of tuples (records or rows). 
Each tuple in a relational table represents an object identified by a unique key and described by a set of attribute values. 
A semantic data model, such as an entity-relationship
(ER) data model, is often constructed for relational databases. 
An ER data model represents the database as a set of entities and their relationships.

## Data Warehouses
A data warehouse is usually modeled by a multidimensional data structure,
called a data cube, in which each dimension corresponds to an attribute
or a set of attributes in the schema, and each cell stores the value of some
aggregate measure, such as count or sum(sales amount). A data cube provides
a multidimensional view of data and allows the precomputation and fast access
of summarized data.

### Example:
Suppose that Flipkart is a successful Indian company, with branches
around the world. Each branch has its own set of databases. The president of
Flipkart has asked you to provide an analysis of the company’s sales per
item type per branch for the third quarter. This is a difficult task, particularly
since the relevant data are spread out over several databases, physically located
at numerous sites.
If Flipkart had a data warehouse, this task would be easy. 
A data warehouse is a repository of information collected from multiple sources, stored
under a unified schema, and usually residing at a single site. Data warehouses
are constructed via a process of data cleaning, data integration, data transforma-
tion, data loading, and periodic data refreshing. This process will be discussed
in Chapters 3 and 4. Figure 1.6 shows the typical framework for construction
and use of a data warehouse for Flipkart.
To facilitate decision making, the data in a data warehouse are organized
around major subjects, such as customer, item, supplier, and activity. 

## Transactional Data
In general, each record in a transactional database captures a transaction,
such as a customer’s purchase, a flight booking, or a user’s clicks on a Web page.
A transaction typically includes a unique transaction identity number (trans ID)
and a list of the items making up the transaction, such as the items purchased
in the transaction. 
A transactional database may have additional tables, which
contain other information related to the transactions, such as item description,
information about the sales person or the branch, and so on.

data mining on transactional data can do so by mining frequent itemsets, that is, sets of items that are frequently sold together. 

### Example
A transactional database for Flipkart. Transactions can be stored
in a table, with one record per transaction. From the relational database
point of view, the sales table is a nested relation because the
attribute “list of item IDs” contains a set of items. 
Because most relational database systems do not support nested relational structures, the transactional database is usually either stored in a flat file in a format similar to that or unfolded into a standard relation in a format similar to that of the items sold table

## Other Kinds of Data
Besides relational database data, data warehouse data and transaction data,
there are many other kinds of data that have versatile forms and structures and
rather different semantic meanings. 
Such kinds of data can be seen in many applications, such as time-related or sequence data (e.g., historical records, stock exchange data, time-series and biological sequence data), data streams (e.g.,video surveillance and sensor data, which are continuously transmitted), spatial data (such as maps), engineering design data (such as the design of buildings,system components, or integrated circuits), hypertext and multimedia data (in-
cluding text, image, video, and audio data), graph and networked data (such
as social and information networks), and the World Wide Web (a huge, widely
distributed information repository made available by the Internet). 
These applications bring about new challenges, like how to handle data carrying special
structures (such as sequences, trees, graphs and networks) and specific seman-
tics (such as ordering, image, audio and video contents, and connectivity), and
how to mine patterns that carry rich structures and semantics.

Various kinds of knowledge can be mined from such kinds of data. Here,
we list just a few.
Regarding temporal data, for instance, we can mine banking
data for trends of changes, which may aid in the scheduling of bank tellers
according to the volume of customer traffic. 
Stock exchange data can be mined to uncover trends that could help you plan investment strategies 

It is important to keep in mind that, in many applications, multiple types
of data are present. For example, in Web mining, there often exist text data on
Web pages, multimedia data (e.g., pictures and videos) on Web pages, graph
data like Web graphs, and map data on some Web sites.