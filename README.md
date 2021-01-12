# Circs (work in progress)

Circs is a module for investigating graphs in databases of financial transactions in the absence of a graph database such as Neo4j.

## Why?

Circs addresses two related problems:

1. Databases of transactions need to become graphs

With synthetic datasets of financial data becoming increasingly common (c.f. https://www.fca.org.uk/firms/innovation/regulatory-sandbox, https://data.europa.eu/euodp/en/data/dataset/CJ63n6pnha3LiEO6McA, https://mostly.ai/industries/synthetic-data-for-finance/) it has occurred on multiple occasions that I have had access to transaction-ecosystem data in a Postgres database. Circs provides bits of code to help you quickly get medium or small chunks of these data into graphs for network analysis.


2. Graph analysis packages need to be optimised for financial networks

In FinTech, there is increasing interest in smart money on the network level. Circs builds on top of networkx to implement a few concepts from financial networks which are of use to analysts. The most important of these are Cliques and Circs - a pruned k-core of a specificied subgraph.

