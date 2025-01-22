![Image image_filename](solution_sign.png)
    
# Epic Caboodle 

## A learning pathway for epic caboodle certification.

    
![Solution](code.png)

    

# Caboodle   CDW110v Caboodle Data   Model Fundamentals

## Caboodle  Table of Contents
 
1. Introduction
2. The Basics Of Caboodle
3. Investigating Caboodle
4. Change Tracking
5. Referential Integrity
6. Beyond Facts and Dimensions
7. Appendix A Completing Your Training Track
8. Appendix B End User Badge Guide
9. Appendix C Additional Practice
10. Appendix D Lesson 1 4 Review



# Chapter 1 Introduction to Caboodle Data Model Fundamentals 

Welcome to Caboodle Data Model Fundamentals! This course introduces the basic tools, structures, and
concepts needed to understand and report on Caboodle data. You will learn the **organizational structure**
of the warehouse, key terms, and resources to help you better leverage Caboodle to write reports. Youll
get a chance to explore and navigate the Caboodle portion of the **Cogito Data Dictionary** and apply what you learn
by writing and evaluating SQL queries against sample data.

Caboodle is a powerful analytics tool that can store custom data from Epic and non Epic sources. While
this course cannot predict every data point that will end up in your Caboodle database, it can familiarize
you with the data model and the accompanying documentation so that you can make the most out of
what Caboodle has to offer.

#### This material contains confidential and copyrighted information of Epic Systems Corporation



# EPIC Training Caboodle  Chapter 2  The Basics of Caboodle

## Introduction **The Basics of Caboodle**

Caboodle provides a framework for combining **Epic** and **non   Epic** data in a single, unified data model that
has been designed for efficient reporting. This database is one reporting tool in **Epics Cogito ergo sum
Enterprise Intelligence suite**. Caboodle can help your organization get more value from the information in
your system and broaden the scope of analytical reporting.

By the End of This Lesson, You Will Be Able To...
1. Describe **how Caboodle is populated**
2. Describe **Caboodles schemas** and identify which one report writers use
3. Identify the **naming conventions** used in Caboodle
4. Describe how **Caboodle fits with Epics reporting tools**


## What is Caboodle ?

**Caboodle** in its simplest sense is a **data warehouse**, designed to store **Epic** and **non Epic data**. A data
warehouse is a relational database, made up of tables and columns, which can be queried using SQL.

But Caboodle is more than just a data warehouse. Caboodle also includes

1. The **extract, transform, and load (ETL)** process that moves data into the data warehouse
2. The **infrastructure and tools** used for managing and monitoring the system
3. The **Caboodle Console**, a web application containing a set of **administrative tools**

#### Data in Caboodle

The Caboodle data warehouse stores data from multiple sources, both Epic and non Epic. To fully
understand the relationships between data points, you must understand where the data comes from, and
the meaning of the data entered in the system.


## Flow of Data into Caboodle



## What is Chronicles ?

**Chronicles** is Epics production database. End users enter data into Chronicles through their daily
activities. This database is **hierarchical** and requires its own **reporting tools**. As the source for all Epic data,
Chronicles contains definitions for how certain pieces of data may be stored and the relationships
between those pieces of data.

page 15



## What is Clarity ? 

**Clarity** extracts data from the Chronicles database through a standard **ETL** process. After transformation,
the data is stored in a relational database on a separate server. Even though the structure of the
Chronicles and Clarity databases differ significantly, the Clarity ETL process **preserves the relationships
mapped in Chronicles**.

Understanding the Clarity data model can help you investigate **data lineage** in Caboodle. If you are not
familiar with the Clarity data model, consider working with a **Clarity BI developer** when you need to know
more about the origins of a particular data point.

page 15



## What is Caboodle ? 

**Caboodle** can receive data from Clarity **Epic data** and from other databases **non Epic data**. Once
again, the **relationships** between data are preserved during the Caboodle ETL process. There are two
databases within Caboodle

1. the **staging database**
2. the **reporting database** 

Data first moves from its source into the staging database. 
Here data is transformed, checked for data integrity issues, and cleaned to resolve those issues. 
Once the data is ready, it is moved to the reporting database. 
This is the database used by Caboodle report writers to create reports.



## Data Model Component Naming Convention

Tables in Caboodle do not stand alone, each is considered part of a Data Model Component (DMC). A
DMC consists of the table, the packages used to populate the table, and underlying metadata tables that
assist Caboodle Administrators with the ETL process. Each DMC has a type, and each type has a specific
naming convention. These naming conventions are strictly enforced in Caboodle, allowing a tables suffix
to provide information about its structure and purpose. These suffixes are

  **Dim for dimensions**
Dimension tables (frequently referred to as dim tables due to their suffix) contain one row for each
entity within the set. Examples include a medication (MedicationDim), a patient (PatientDim), a provider
(ProviderDim). Compared to fact tables, dimension tables generally contain more data and fewer lookup

  **Fact for facts**
Fact tables contain one row for each occurrence of some significant, measurable event. Examples include
a provider placing an order for a medication (MedicationOrderFact) or a patient having an encounter
(EncounterFact). Fact tables tend to have quite a few lookup columns pointing to dimension tables.
While reporting out of Caboodle, the majority of the tables you will use will be facts and
dimensions.

  **Bridge for bridges**
Bridge tables are used in Caboodle to model many to many relationships. Examples include a patient
with many diagnoses on their problem list (DiagnosisBridge) or an authorization with many procedures
associated with it (ProcedureBridge). Bridge tables will be covered in more detail in Beyond Facts and
Dimensions.

 **DataMart for data marts**
Data marts are used in Caboodle to store data points from several DMCs in one place. If you were going
to report on hospital admissions and subsequent readmissions, you would likely use
HospitalReadmissionDataMart instead of using HospitalAdmissionFact.

  **AttributeValueDim for EAV tables**
Entity Attribute Value (EAV) dimension tables contain information about values of additional attributes in
Caboodle. The EAV structure will be covered in more detail in COG240 Clinical Data Model.

  **<suffix>X for custom tables**
Caboodle is customizable. When you are working with the Caboodle at home, you may find tables of any
type (fact, dim, bridge etc.) that ends in an X. When a DMCs name ends with X, you know that a Caboodle
developer at your organization has created this custom DMC.




## What is SQL Server Integration Services ? 

**SQL Server Integration Services** (SSIS) packages are the mechanism used to move data during the
Caboodle ETL process.
In training, you will see references to Epic released SSIS packages that extract data to Caboodle. While
most of these packages extract Clarity data, Epic has released some packages that extract additional data
sets based on existing agreements with other vendors. Epics Caboodle development team continues to expand the library 
of available SSIS packages, so if a particular data point does not exist in Caboodle at this time, it may get extracted in 
the **future**.

**Your organization** can create **custom SSIS packages** to extract Clarity data or additional data sets.



## Schemas in Caboodle

In relational databases, a schema is a collection of database objects. Schemas allow content to be grouped
together for many different purposes, such as filtering for service area. There are three Epic released
schemas in Caboodle relevant to report writers.

1. The **dbo schema** is the data source for SlicerDicer. The Caboodle Dictionary in the Caboodle
Console and the Caboodle portion of the Cogito Data Dictionary reflect the contents of the dbo
schema.

2. The **FullAccess schema** contains everything for report writers from the dbo schema and more. For
example, many columns in dbo are known as **binary columns** because they only contain values of
**1 or 0**. In FullAccess, many of these columns have a paired column that contains values of **Yes and
No** instead of **1 and 0**. FullAccess should be your **default schema** for reporting.


3. The **FilteredAccess schema** is similar to the FullAccess schema except report writers who only
have access to the FilteredAccess schema will have their results filtered based on their user
security. FilteredAccess is commonly used with **Community Connect organizations**.
 



## Why Use Caboodle?
There are several advantages to using Caboodle.

### Caboodle can house Epic and Non Epic Data

**Caboodle** provides an infrastructure for combining **Epic** and **non Epic** data. In some cases, space has been
provided for data that will not be populated by Epics software but that your organization might want to
extract from a non Epic source. This includes items like the responses from patient satisfaction surveys,
information about charge costs, and paid claims data. In addition, custom data packages can be written by
Caboodle developers to accommodate your organizations reporting needs.

### Hyperspace Integration

Hyperspace is Epics main front end program. The vast majority of workflows done by end users, including
data entry workflows, are done in Hyperspace. Within Hyperspace are many applications, each
specializing in certain areas. SlicerDicer is one such application. SlicerDicer is Epics self service reporting
tool. It dynamically queries Caboodle data based on selected criteria, slices, and measures. This provides
Hyperspace end users the ability to explore analytical data without requiring technical knowledge of SQL.
Since Caboodle queries form the foundation of this tool, BI Developers with a working knowledge of the
Caboodle data model and documentation tools can troubleshoot SlicerDicer queries and better
understand the underlying data.

Certain Radar metrics and Workbench templates can also query Caboodle data. Cogito Tools
administrators can create custom Radar metrics and Workbench templates to meet end user needs.

Cogito BIDs are able to investigate both Clarity and Caboodle reporting options directly in the Analytics
Catalog. This will help report writers find the most convenient reporting option and visualize what Clarity columns are brought 
into Caboodle.



## Enforced Naming Conventions

Another **advantage to using Caboodle** is the **enforced naming convention** of the database. All tables and
columns will be written using **PascalCase**. The first letter in each word will be capitalized without
underscores between the words.

## Key Columns in Caboodle
Report writers who have worked with relational databases are familiar with the idea of a key used to
identify a row in a table. **All key columns** in Caboodle are **surrogate keys** including **primary keys** and
**lookup columns**.

**Surrogate Key**   Any key column where the columns value does not exist in the source database
and is created during the ETL process. In Caboodle all columns that end in Key are surrogate
keys. This is necessary because Caboodle contains both Epic and non Epic data.
Lookup Column   A column in one table whose value identifies at least one row in another table.

Most tables in Caboodle have at least one **lookup column**. **Lookup columns** in Caboodle will always
end in Key and the Cogito Data Dictionary will tell report writers what table the lookup column
references.

For many DMCs (Data Model Components) in Caboodle the primary key will follow a strict naming
convention. For PatientDim, the primary key is PatientKey. PatientKey is a surrogate key, which means the
value stored in Caboodle does not exist in the source databases. If you are looking for identifying
information for validation in Caboodle, consider using the **EpicId** or **EpicCsn** columns. Columns that end
in **EpicId** and **EpicCsn** store source database identifiers.



## Data Model Component Naming Convention

Tables in Caboodle do not stand alone, each is considered part of a **Data Model Component (DMC)**. A
DMC consists of 
1. the table 
2. the packages used to populate the table
3. underlying metadata tables that assist Caboodle Administrators with the ETL process. 

Each DMC has a type, and each type has a specific naming convention.
These naming conventions are strictly enforced in Caboodle, allowing a tables suffix
to provide information about its structure and purpose. These suffixes are

1. **Dim for dimensions** Dimension tables frequently referred to as **dim tables** due to their suffix contain one row 
for each entity within the set. Examples include a medication **MedicationDim**, a patient **PatientDim**, a provider
**ProviderDim**. Compared to fact tables, dimension tables generally contain more data and fewer lookup columns.

2. **Fact for facts** Fact tables contain one row for each occurrence of some significant, **measurable event**. Examples include
a provider placing an order for a medication **MedicationOrderFact** or a patient having an encounter
**EncounterFact**. **Fact tables** tend to have quite a few lookup columns pointing to dimension tables.

3. **Bridge for bridges**  Bridge tables are used in Caboodle to model **many to many relationships**. 
Examples include a patient with many diagnoses on their problem list **DiagnosisBridge** or an authorization with many
procedures associated with it **ProcedureBridge**. Bridge tables will be covered in more detail in Beyond Facts and
Dimensions.

4. **DataMart for data marts** Data marts are used in Caboodle to store data points from several DMCs in one place. If you were
going to report on hospital admissions and subsequent readmissions, you would likely use HospitalReadmissionDataMart instead of
using HospitalAdmissionFact.

5. **AttributeValueDim for EAV tables** Entity Attribute Value **EAV** dimension tables contain information about values of 
additional attributes in Caboodle. The EAV structure will be covered in more detail in COG240 Clinical Data Model.
 <suffix>X for custom tables
 
**Caboodle is customizable**. When you are working with the Caboodle at home, you may find tables of any
type **fact, dim, bridge etc.** that ends in an X. When a DMCs name ends with X, you know that a Caboodle
developer at your organization has created this custom DMC.
 


**SQL Server Integration Services (SSIS)** is a component of Microsoft SQL Server used for data integration and workflow applications. Heres a brief overview of what SSIS is and what it does

1. **Data Extraction, Transformation, and Loading (ETL)**  
    SSIS helps you **extract** data from various sources (e.g., databases, flat files, Excel, or cloud sources), **transform** it (clean, merge, aggregate, or apply business logic), and **load** the refined data into a target system (e.g., a data warehouse).  

2. **Automation and Workflow**  
    In addition to ETL tasks, SSIS includes tools for building **automated workflows**—for example, you can automate tasks like sending email notifications, running SQL scripts, or executing other applications when a data load finishes.

3. **Builtin Components and Extensions**  
    SSIS offers a variety of **builtin data transformation** components (e.g., merge joins, lookups, data conversion) and also allows you to create custom scripts or use thirdparty extensions to handle more complex scenarios.

4. **Integration with SQL Server**  
    Because SSIS is part of SQL Server, it integrates well with **SQL Server Management Studio** and other SQL Server components, making it easier to administer and schedule packages.

5. **Visual Development Environment**  
    SSIS projects are often created and maintained in a **visual designer** (found in **SQL Server Data Tools**), allowing you to drag and drop tasks, connect data flows, and configure properties without extensive coding.

**In short** SSIS is a powerful tool for orchestrating data movement and transformations, enabling organizations to consolidate data from diverse sources into a single repository for reporting, analysis, or further processing.



## Simplified Report Writing

Like many other data warehouses, **Caboodle** uses a **dimensional data model**. Dimensional data models
arrange tables in a way that makes queries faster to write and more efficient to run when compared to
other structures.

1. **Accessibility** Dimensional data models are designed to be intuitive, therefore Caboodle requires
less training for business intelligence developers than other platforms.
2. **Efficiency** It is generally quicker and more efficient to write a report using Caboodle versus Clarity,
Epics other relational database.
3. **Fewer tables and simpler joins** Reports written using Caboodle tend to have shorter run times
since they require fewer tables and fewer multi column joins, which improves run time efficiency for reports.

The trade off for these advantages is that dimensional data models require a more complicated ETL
process to maintain.



## The Star Schema

Many reports in Caboodle center around events and thus around fact tables. It is more common to focus
a report on measurable events **medication orders, patient encounters, billing transactions) than on the
entities involved with those events (medications, patients, providers**. While report writers may
occasionally be asked to write a report about the providers at their organization, they will more frequently
be asked to write reports about something those providers did **placing a medication order** or were
involved with **treating a patient during an encounter**.

The **star schema** refers to the way that reports centered around fact tables appear in a **join diagram**. A
fact table contains all of the entities that were involved with each event, but little additional information
about the entities. If a report needs that additional data, joins must be made to the appropriate dimension
tables. This is where the star schema takes shape.

**MedicationOrderFact** contains lookup columns indicating which medication was ordered, for which patient
it was ordered, and which provider ordered it, but it does not contain any additional information about
those entities such as their names. The associated dimensions tables for each entity stores that
information. A report about medication orders should include the name of the medication. To include that,
we must join to MedicationDim.



## Key Terms for study check list 

1. **ETL** A process that involves extracting data from sources, transforming it to fit operational needs, and loading it into a target system or database.  
2. **Staging database** A temporary, intermediary database designed to hold raw or lightly transformed data before further processing or loading into the final destination.  
3. **Reporting database** A dedicated database optimized for running queries, analytics, and reports, often holding summarized or aggregated data.  
4. **SSIS package** A deployable unit in **SQL Server Integration Services** containing the definitions and tasks needed to move and transform data between sources and destinations.  
5. **dbo schema** The default schema in SQL Server that typically contains the core objects (tables, views, stored procedures) created by database owners.  
6. **FullAccess schema** A custom schema (in some systems) intended to allow unrestricted read and write access to its database objects.  
7. **FilteredAccess schema** A custom schema used to control or limit the visibility and operations on its data, often enforcing specific security or business rules.  
8. **Surrogate key** An artificial, systemgenerated unique identifier used as the primary key instead of a business specific (natural) identifier.  
9. **Source identifier** A field that indicates where a specific record originated, helping track data lineage in multi system environments.  
10. **Primary key** A column or set of columns that uniquely identifies each row in a table, enforcing uniqueness and preventing duplicate records.  
11. **Lookup column** A column used to reference related data in another table, enabling relational lookups and joins.  


## Study Checklist

1. Identify the benefits of using Caboodle
2. Identify columns in a table that contain Epic identifiers
3. How does data flow into Caboodle 
4. The relationship between **Slicer dicer and caboodle** SlicerDicer is Epics self service reporting tool in Hyperspace that dynamically queries Caboodle data.


## Chapter 3  Investigating Caboodle 

1. Introduction
2. Navigating the Cogito Data Dictionary
3. The Overview Section
4. The Columns Section
5. Lineage
6. Reporting Availability
7. ER Diagram Section
8. Dependencies
9. Indexes
10. Packages
11. Advanced
12. Additional Navigation
13. Exercise 3 1  Investigating Caboodle
14. Research Tools
15. Reporting with Caboodle
16. SlicerDicer Troubleshooting Queries
17. Join Diagrams
18. Exercise 3 2 Creating a Join Diagram and Writing a Query
19. After Class Exercise 3 1  Research using SlicerDicer Troubleshooting
20. Reviewing the Chapter


## Introduction to chapter 3 investigating Caboodle

The **Cogito Data Dictionary** is your roadmap for writing reports with the Caboodle database. It contains
descriptions of **tables and columns**, important characteristics of each database object, table level and
column level data lineage, information to help identify joins, and more. Other documentation on Galaxy is
also available to learn more about reporting on unfamiliar topics and new database objects as Epic
releases them.

### By the End of This Lesson, You Will Be Able To 
1. **Investigate Caboodle tables** using the **Analytics Catalog**
2. Search the **Analytics Catalog** for a Caboodle table using an INI and item number
3. Open a table in the **Analytics Catalog** to investigate the columns
4. Identify the **granularity** of a table in Caboodle
5. Identify the **data lineage for a Caboodle table**
6. Identify the **data lineage for a Caboodle column**
7. Use **Caboodles ER diagrams** to research database objects


The content found in the Cogito Data Dictionary through Hyperspaces **Analytics Catalog** is
also available in the Caboodle Dictionary in the Caboodle Console. As they effectively capture
the same Caboodle documentation and the Cogito Data Dictionary is the primary reporting
resource, this class will **not cover the Caboodle Dictionary in the Caboodle Console**.


## Navigating the Cogito Data Dictionary

The **Caboodle Dictionary** is now completely integrated within the **Analytics Catalog** as part of the Cogito
Data Dictionary in Hyperspace. When you are researching Caboodle database objects, you will find them
in the same location as all of Epics reporting content.

1. **Log in to Hyperspace** as a BID (user ID 6001##, password train).
2. Open the **Analytics Catalog**.
3. **Filter** the content in the Analytics Catalog to the **Data Dictionary.**
4. **Use the search bar** to search for EncounterFact. 



## The Overview Section

The Overview section is the top section when viewing a database object in the Analytics Catalog. It
displays
1. A **description of the database object**.
2. **Chips that provide some information** about the database object including the type of database
object.
3. The **granularity of** the database object.



## The Columns Section
 
The **Columns section** is directly below the overview section and lists out some key information about the
columns including
1. **Name** the name of the column in the Caboodle database. 
2. **Data Type** the data type of the column
3. **Available** the available column will have a SD icon if SlicerDicer can report on the column. 
4. **Links to** Populated for lookup columns. The Links to section lists out the database object that
the lookup column references.
5. **Chronicles Info** The items in Chronicles that are documented in the columns data lineage.
6. **Description** A brief description of the column. If the description is too large to fit in that cell, click
on the chevrons to expand out that cell to display the full description.


## ER Diagram section

Facts and data marts will include an **ER Diagram section** after the Columns section. The ER Diagram
section will be built in a classic star schema format with the table you are investigating in the center and
all of the tables it can reference around it. To investigate the possible joins, click on one of the lookup
columns in EncounterFact, or one of the identifying columns in one of the exterior tables.

There may be more than one possible option to join two tables. If there is a durable key available, this is
the recommended lookup column to use with the condition <LookupTable>.IsCurrent = 1. The **Change
Tracking lesson**  will elaborate on why this is the case.

## Dependencies

The **Dependencies section** indicates what database objects a table is dependent on. For tables in
Caboodle, these might be Clarity tables and columns or other Caboodle tables and columns. You
are provided with the tables and columns that the table is dependent on.

## Indexes

The **Indexes section** lists which columns (if any) are indexed in this table. Indexed columns can
improve the efficiency of your query compared to non indexed columns when used in logical expressions
in a SQL query.

## Packages

The **Packages section** is the last section in the dictionary. It lists the Epic released and custom SSIS
packages that populate the table and their queries. It is possible for more than one SSIS package to
populate a table in Caboodle. It is also possible for multiple sources to populate a table in Caboodle.

## Advanced

The **Advanced section** lists metadata tables that are part of this DMC which are used during ETL. You can
learn more about them in COG280 Cogito Systems Administration I, but they will not be relevant to this



## Lineage

The **Source Data Lineage** section is available in the expanded column information. It contains the source
column information documented by the Caboodle developer. If the column is populated with Epic data,
the source column information will be Clarity tables and columns and there will also be a section listed as
Chronicles Info. The Chronicles Info section will display the INI and item number of the items that
populate the Clarity column.

If the information in the Source Data Lineage section is not detailed enough, expand out the Package
Lineage Details for some more information on the columns and the logic used to populate the column in
Caboodle. 

## Reporting Availability

The **Reporting Availability** section of the column information section reveals how the column can be used
in SlicerDicer sessions. The different filter records that utilize the column will be listed. To learn which data
models can use those filter records, use the Record Viewer.


## Research Tools
For the report request in Exercise 1, the report requester had some previous knowledge about Caboodle
and was able to recommend a fact table to use in the report. When the report requester is unable to
provide identifying information, it will be important that you can identify tools for researching reporting
topics in Caboodle.

## Reporting with Caboodle
The Reporting with Caboodle guide includes descriptions and reporting examples for most of the tables in
Caboodles reporting database. The document provides a series of reporting topics, which are broken
down into scenarios and examples for learning to work with the Caboodle tables. Each topic includes
common tables, example reports, and an exercise for furthering your knowledge about the topic.
When you are assigned a report request on a topic that you are not familiar with, Reporting with
Caboodle is a great starting resource for you to investigate prior to searching the Analytics Catalog.

## SlicerDicer Troubleshooting Queries
Another resource for researching Caboodle is the SlicerDicer troubleshoot button. If you have access to
the troubleshooting button in SlicerDicer you have access to the underlying query that is helping to
construct the data visualizations in SlicerDicer. Often if you are attempting to create a report that is similar
to one you can produce in SlicerDicer, this is a way to know which database objects you want to explore
and research more.


## Enforced Naming Conventions

Another advantage to using Caboodle is the enforced naming convention of the database. All tables and
columns will be written using PascalCase. The first letter in each word will be capitalized without
underscores between the words.

### Key Columns in Caboodle

Report writers who have worked with relational databases are familiar with the idea of a key used to
identify a row in a table. All key columns in Caboodle are surrogate keys including primary keys and
lookup columns.

 **Surrogate Key**   Any key column where the columns value does not exist in the source database
and is created during the ETL process. In Caboodle all columns that end in  Key are surrogate
keys. This is necessary because Caboodle contains both Epic and non Epic data.

 **Lookup Column**   A column in one table whose value identifies at least one row in another table.
Most tables in Caboodle have at least one lookup column. Lookup columns in Caboodle will always
end in  Key and the Cogito Data Dictionary will tell report writers what table the lookup column
references.

For many DMCs (Data Model Components) in Caboodle the primary key will follow a strict naming
convention. For PatientDim, the primary key is PatientKey. PatientKey is a surrogate key, which means the
value stored in Caboodle does not exist in the source databases. If you are looking for identifying
information for validation in Caboodle, consider using the  EpicId or  EpicCsn columns. Columns that end
in  EpicId and  EpicCsn store source database identifiers.



## Join Diagrams

**Join diagrams** are visual representations of the tables, columns, and joins involved in a query. They are
similar in appearance to ER diagrams. However, unlike ER diagrams, which show all possible joins from a
certain table, join diagrams show only the joins that will be used in a certain report. They allow report
writers to map out a query before writing the code, making the process of writing the code easier and
more efficient. Join diagrams can be especially helpful for report writers who are new to SQL, but they are
beneficial to anyone.

In the example below, we have been asked to write a report about patient encounters that took place in
the year 2020. The report should include the patients name, the providers name, and the date on which
the encounter took place.

A simple join diagram. The asterisks  indicate the primary key columns for each table. The lines between
tables show the two columns that will be used in each join condition.


## Schema SQL 

select schema_Name()

select top 100 Isleaked, Isleaked_YESNo
FROM fullaccess.ReferralFact
where Count = 1 and _IsInferred = 0 

select top 100 ReferralKey, Isleaked 
FROM dbo.ReferralFact
where Count = 1 and _IsInferred = 0 


## Chapter 3  Investigating Caboodle

### Introduction

The **Cogito Data Dictionary** is your **roadmap** for writing reports with the Caboodle database. It contains
descriptions of tables and columns, important characteristics of each database object, table level and
column level data lineage, information to help identify joins, and more. Other documentation on Galaxy is
also available to learn more about reporting on unfamiliar topics and new database objects as Epic
releases them.

By the End of This Lesson, You Will Be Able To...
 Investigate Caboodle tables using the Analytics Catalog
 Search the Analytics Catalog for a Caboodle table using an INI and item number
 Open a table in the Analytics Catalog to investigate the columns
 Identify the granularity of a table in Caboodle
 Identify the data lineage for a Caboodle table
 Identify the data lineage for a Caboodle column
 Use Caboodles ER diagrams to research database objects


## Navigating the Cogito Data Dictionary

The **Caboodle Dictionary** is now completely integrated within the **Analytics Catalog** as part of the Cogito
Data Dictionary in Hyperspace. When you are researching Caboodle database objects, you will find them
in the same location as all of Epics reporting content.


### The Overview Section

The Overview section is the top section when viewing a database object in the Analytics Catalog. It
displays
 A description of the database object.
 Chips that provide some information about the database object including the type of database object.
 The granularity of the database object.


### The Columns Section

The Columns section is directly below the overview section and lists out some key information about the
columns including




## Lineage

The **Source Data Lineage** section is available in the expanded column information. It contains the source
column information documented by the Caboodle developer. If the column is populated with Epic data,
the source column information will be Clarity tables and columns and there will also be a section listed as
Chronicles Info. The Chronicles Info section will display the INI and item number of the item(s) that
populate the Clarity column.

If the information in the Source Data Lineage section is not detailed enough, expand out the Package
Lineage Details for some more information on the columns and the logic used to populate the column in
Caboodle.


## Reporting Availability
The Reporting Availability section of the column information section reveals how the column can be used
in SlicerDicer sessions. The different filter records that utilize the column will be listed. To learn which data
models can use those filter records, use the Record Viewer.




## ER Diagram Section
  Navigate to the ER Diagram section by scrolling down or clicking on the ER Diagram tab.
3 • 5 Investigating Caboodle
 
Facts and data marts will include an ER Diagram section after the Columns section. The ER Diagram
section will be built in a classic star schema format with the table you are investigating in the center and
all of the tables it can reference around it. To investigate the possible joins, click on one of the lookup
columns in EncounterFact, or one of the identifying columns in one of the exterior tables.


There may be more than one possible option to join two tables. If there is a durable key available, this is
the recommended lookup column to use with the condition <LookupTable>.IsCurrent = 1. The Change
Tracking lesson will elaborate on why this is the case.




## Dependencies
The Dependencies section indicates what database objects a table is dependent on. For tables in
Caboodle, these might be Clarity tables and columns or other Caboodle tables and columns. You
are provided with the tables and columns that the table is dependent on.


## Indexes
The Indexes section lists which columns (if any) are indexed in this table. Indexed columns can
improve the efficiency of your query compared to non indexed columns when used in logical expressions
in a SQL query.


## Packages
The Packages section is the last section in the dictionary. It lists the Epic released and custom SSIS
packages that populate the table and their queries. It is possible for more than one SSIS package to
populate a table in Caboodle. It is also possible for multiple sources to populate a table in Caboodle.

## Advanced
The Advanced section lists metadata tables that are part of this DMC which are used during ETL. You can
learn more about them in COG280 Cogito Systems Administration I, but they will not be relevant to this class.

## Additional Navigation
After investigating the possible join with CoverageDim, you are curious to learn more about that table.



## Join Diagrams

Join diagrams are visual representations of the tables, columns, and joins involved in a query. They are
similar in appearance to ER diagrams. However, unlike ER diagrams, which show all possible joins from a
certain table, join diagrams show only the joins that will be used in a certain report. They allow report
writers to map out a query before writing the code, making the process of writing the code easier and
more efficient. Join diagrams can be especially helpful for report writers who are new to SQL, but they are
beneficial to anyone.

In the example below, we have been asked to write a report about patient encounters that took place in
the year 2020. The report should include the patients name, the providers name, and the date on which
the encounter took place.

## A  example join Diagram 

![join_diagram.png](attachmentjoin_diagram.png)



## Chapter 4  Change Tracking

### Introduction

In a previous lesson, you learned about Caboodle surrogate keys. In this lesson, you will learn the purpose
of durable key columns, special surrogate key columns used with snapshot tables. You will learn how to
identify snapshot data and how to return the current values from snapshot tables.

By the End of This Lesson, You Will Be Able To...

1. Predict how Caboodle will change when source data is changed
2. Identify **snapshot data** in Caboodle
3. Identify the purpose of the **durable key**
5. Join to **snapshot tables** to return **current data**
6. **Summarize data** when snapshot change tracking is used


## Change Tracking
**Change tracking** indicates how Caboodle will update a table when there are changes to its source data. In
Caboodle, there are two types of change tracking that are possible.

1. Snapshot Change Tracking (Type 2)
2. None (Type 1)


If a table is using **Snapshot** change tracking (also called Type 2), there will be a chip in the overview
section of the table that states this. These tables will track changes to the snapshot data. If no chip is
present, the table, and all of its columns, are considered **Non snapshot, or Type 1**.



### NonSnapshot Data

Many Caboodle tables do not use change tracking. These tables reflect the current content of the source
data at the time of the most recent extract. The granularity of these tables is simply one row per entity
extracted to the table. For example, each row of **EncounterFact** represents one encounter. If there is an
update to an encounters data, then in the next extract Caboodle will update the relevant values for the
row.

DepartmentDim is a non snapshot table. If a departments abbreviation is updated in the source database,
Caboodle would only store the updated value.

### Snapshot Data

Some Caboodle tables and columns use change tracking, which allows them to store both current data
and historical data. These are known as snapshot tables and columns. To identify a snapshot table, look
for a chip in the overview section that says **Snapshot (Type 2)**. The granularity of snapshot tables is one
row per entity for a date range. For example, each row in PatientDim represents the data for one patient,
as it existed in Caboodle, during a particular date range. Thus, there can be multiple rows for the same
patient, each one corresponding to different date range.


Caboodle creates a new snapshot row if the source data for any **snapshot** column has changed and labels
the rows with ETL dates. The new row stores the new snapshot values, and old rows retain their snapshot
values. Therefore, each row is effectively a snapshot of the data as it once appeared in Caboodle. For
each entity, there is exactly one row that stores current information, while the remaining rows contain old
data that is no longer current in the source. When using snapshot tables, additional filtering is needed to
ensure that only current data is returned.
 

## Identifying Snapshot Data


A **snapshot table** has **one or more snapshot columns**. **Snapshot columns retain previous values** which
been extracted to Caboodle and have since changed in the source. This change could be an update to
existing data or a deletion. For snapshot tables in the Columns section of the dictionary, you will be able
to sort by a column Snapshot. Only snapshot columns will track changes found at ETL.


 
## Extra Columns in Snapshot Tables

Snapshot tables have additional columns to help make sense of data in the table.

## Durable Key

The granularity of PatientDim is a patient record for a date range, so that is what the PatientKey is
identifying. The **DurableKey column** identifies unique entities in the table. In the case of PatientDim, the
**DurableKey** is used to identify unique patients. When summarizing snapshot data, you most likely want to
summarize using the DurableKey instead of the primary surrogate key.

## StartDate and EndDate

The **StartDate** and **EndDate** columns store the date range for the snapshot data in the table. These
represent the ETL dates during which a rows snapshot data was valid. For the rows that hold the earliest
and most recent versions of the data recorded in **Caboodle**, the **StartDate and EndDate** are set to a default
start and end date value of **111979** and **12312099**.

## IsCurrent
The **IsCurrent** column is a flag that stores the value of 1 if the row holds the most current information and
0 otherwise. For a given DurableKey value, there will be **exactly 1 row that is current**. The **current row**
should be referenced for Caboodle reports.


 
## Referencing Snapshot Data

It is very common for reports to join to snapshot tables. For example, consider a report about employees
who are referenced in a billing transaction. 

If this join was completed using the condition
BillingTransactionFact.EmployeeKey = EmployeeDim.EmployeeKey

Then it would be possible to return data that is no longer current. For example, applying this condition to
the first row in BillingTransactionFact (BillingTransactionKey = 111) would return the row where Nathan
was a High School Teacher, which is no longer true.

If the join was completed using the condition
BillingTransactionFact.EmployeeDurableKey = EmployeeDim.DurableKey

Then it would be possible to return more rows than expected. For example, the first
transaction (BillingTransactionKey = 111) would have two rows in the results one for each row that
represents Nathan Steel in EmployeeDim. The second transaction (BillingTransactionKey = 777) would also
have two rows in the results.

The **correct way** to join to a **snapshot table** is using the **DurableKey** column and filtering with the
**IsCurrent** column
1. BillingTransactionFact.EmployeeDurableKey = EmployeeDim.DurableKey
2. AND EmployeeDim.IsCurrent = 1

By including the condition IsCurrent = 1, you will return only the most current data from your snapshot
tables.


## Exercise 4 2 Office Visit Report

You have been asked to write a report about encounters. The report requester has some Caboodle
knowledge and thought that EncounterFact would be a table to investigate. The requester wants the

following information.
 The encounters Epic CSN value
 The type of encounter (EPT 30)
 The patients name (EPT .2)
 How old the patient was at the time of the encounter in years
 The name of the provider who cared for the patient

This should not be the admitting or attending provider, just the provider associated with the
encounter

 The providers primary specialty (SER 1050)
 The name of department the encounter was in (DEP .2)
 In this exercise, you will use the Analytics Catalog to find the tables and columns that will be needed for
this report. Then try to write the SQL query.


1. Research the Report
2. Use the Analytics

potential SQL 
 select * from EncounterFact.EncounterEpicCsn
 select * from EncounterFact.Type
 select name  from PatientDim.Name
 select * from The patients age in years
 select * from DurationDim.YearsDisplayString
 select * from Providers name .SER .2.
 select * from ProviderDim.Name
 select * from Providers primary specialty
 select * from ProviderDim.PrimarySpecialty
 select * from DepartmentDim.DepartmentName


USE Caboodle_Feb
SELECT 
Type as Encounter_type,
count (distinct EncounterEpicCsn) as Number_of_Encounters,
count (distinct PatientDurableKey) as Number_of_Patients 
FROM EncounterFact
where Type not in(*Deleted,*Not Applicable,*Unspecified,*Unknown) 
group by Type 
order by Number_of_Encounters DESC 


USE Caboodle_Feb
SELECT 
Type as Encounter_type,
TypeCategoryKey,
count (distinct EncounterEpicCsn) as Number_of_Encounters,
count (distinct PatientDurableKey) as Number_of_Patients 
FROM EncounterFact
where Type not in(*Deleted,*Not Applicable,*Unspecified,*Unknown) 
AND Type IN (Office Visit) 
group by Type, TypeCategoryKey 
order by Number_of_Encounters DESC 



 Excercise 43 Lung Screening 

USE Caboodle_Aug

SELECT MAX(PatientDim.PrimaryMrn) Primary MRN
		, MAX(PatientDim.Name) Patient Name
		, COUNT(*) Number of Lung Screening Procedures
	FROM ProcedureOrderFact
		INNER JOIN ProcedureDim
			ON ProcedureOrderFact.ProcedureDurableKey = ProcedureDim.DurableKey AND ProcedureDim.IsCurrent = 1
		INNER JOIN PatientDim
			ON ProcedureOrderFact.PatientDurableKey = PatientDim.DurableKey AND PatientDim.IsCurrent = 1
	WHERE ProcedureDim.IsLungScreeningProgramProcedure = 1
	GROUP BY PatientDim.DurableKey
	ORDER BY 3 desc


 Excercise 43 Lung Screening 

USE Caboodle_Aug

SELECT MAX(PatientDim.PrimaryMrn) Primary MRN
		, MAX(PatientDim.Name) Patient Name
		, COUNT(*) Number of Lung Screening Procedures
	FROM ProcedureOrderFact
		INNER JOIN ProcedureDim
			ON ProcedureOrderFact.ProcedureDurableKey = ProcedureDim.DurableKey AND ProcedureDim.IsCurrent = 1
		INNER JOIN PatientDim
			ON ProcedureOrderFact.PatientDurableKey = PatientDim.DurableKey AND PatientDim.IsCurrent = 1
	WHERE ProcedureDim.IsLungScreeningProgramProcedure = 1
	GROUP BY PatientDim.DurableKey
	ORDER BY 3 desc

## Chapter 5  Referential Integrity


### Introduction

Caboodle has **referential integrity**, which means that **lookup columns will always have a value** and that
value will find a match in the destination table. When a null or unmatched value is loaded into the
Caboodle staging database, the **ETL infrastructure assigns a default value** to the corresponding column in
the reporting database. The value that gets assigned is determined by the circumstances behind the null
or unmatched value as defined by the load package.

In this lesson, you will learn different circumstances that could result in missing or incomplete references
and how Caboodle enforces referential integrity in each.


By the End of This Lesson, You Will Be Able To...
1. Define referential integrity
2. Explain how Caboodle ensures lookup columns will always have a value
3. Explain the meaning of the **minus 1**, **minus 2**, and **minus 3** values in lookup columns
4. Explain how Caboodle ensures lookup columns always have a match
5. Identify inferred rows
6. Explain when an inferred row is created
7. Interpret **Unknown**, **Unspecified**, **Not Applicable**, and **Deleted** values on a report
8. Explain why you may not see inferred or deleted rows in the FilteredAccess



### Referential Integrity

**Referential integrity** is a property of SQL databases. Databases that enforce referential integrity have two
important properties.

1. **Lookup columns** will always have a value even if the source data is null
2. Lookup column values will always have a matching value in the destination table and column

Different databases enforce **referential integrity** in different ways. The rest of this lesson is about how
**Caboodle** does it and how that impacts reports written using Caboodle.



### Ensuring Lookup Columns Always Have a Value

The first principle of referential integrity is that all lookup columns must always have a value. This is
simple when there is a value in the source data. For example, a patient has a primary care provider listed
in Chronicles and Clarity, which we can easily carry forward to Caboodle. But what happens when there
**is not** a value in the source data? There are default values that Caboodle can use to represent this scenario,
each with a different meaning.

## minus 1 equals  **Unspecified Values**

When a lookup columns value is NULL in the source system, the value is said to be unspecified. In this
case, the corresponding lookup column in Caboodle is set to  **minus 1**.

One circumstance that would result in a lookup column having a value of **minus 1** would be a patient who has
not been assigned a primary care physician. When the patients record is loaded into Caboodle, the
PrimaryCareProviderKey column is set to **minus 1**.


## minus 2  equals **Not Applicable Values**

Caboodle is a data warehouse that can load data from multiple sources to populate individual tables. For
any table in Caboodle, it is possible that some columns will not be applicable for every row in the table
based on the load package. One example of this is MedicationDispenseFact. MedicationDispenseFact is a
collection of inpatient and outpatient medication dispenses.



### Ensuring Values in Lookup Columns Always Find a Match

The second principle of referential integrity is that values in lookup columns always find a match in the
destination table. Consider a situation where a patient in PatientDim has a primary care provider in
ProviderDim. Caboodle generates a surrogate key for the provider and uses that value in the lookup
column in PatientDim and in the primary key of ProviderDim.

However, what happens when the lookup column uses one of the default values outlined in the previous
section? These are used when there is no value in the source.



## Inferred Rows

**Referential integrity ensures a match for lookup columns** that already have a match in the destination
table and for default key values like those outlined in the previous section. However, what happens when
a lookup column value does not use one of the default values and also does not have a match in the
destination table?

When this happens in Clarity there is no further action needed because Clarity does not have referential
integrity. On the other hand, Caboodle does have referential integrity, so something must be done. This is
where **inferred rows** enter the picture. In the example above, we can infer that the providers listed for
Forrest and Daniel exist, but Clarity (and thus Caboodle) does not yet know anything about those providers.
When the ETL process loads this data into Caboodle, it will create inferred rows to represent the two
providers.



 Excercise 4.1 

USE Caboodle_Aug;


WITH MostRecentOfficeVisit AS 
	(
	SELECT 	 PatientDurableKey
		, Max(DATE) MostRecentDate
	  FROM EncounterFact 
	    WHERE Type = Office Visit 
			AND DerivedEncounterStatus = Complete
		GROUP BY PatientDurableKey
	)

SELECT MAX(PatientDim.Name) PatientName
		, CAST ( MAX(MostRecentOfficeVisit.MostRecentDate) AS DATE)	Most Recent Office Visit Date
		, CAST ( MAX(EncounterFact.Date) AS date) 2nd Most Recent Office Visit Date
		, DATEDIFF( DAY , MAX(EncounterFact.Date), MAX(MostRecentOfficeVisit.MostRecentDate)) Number of days between Office Visits
		, DATEDIFF( DAY , MAX(MostRecentOfficeVisit.MostRecentDate),CURRENT_TIMESTAMP) Most Recent to Now
		
	FROM EncounterFact
		INNER JOIN MostRecentOfficeVisit
			ON EncounterFact.PatientDurableKey = MostRecentOfficeVisit.PatientDurableKey
			AND MostRecentOfficeVisit.MostRecentDate > EncounterFact.Date
			AND EncounterFact.Type = Office Visit
		INNER JOIN PatientDim
			ON EncounterFact.PatientDurableKey = PatientDim.DurableKey
				AND PatientDim.IsCurrent = 1
		GROUP BY EncounterFact.PatientDurableKey





## Chapter 6  Beyond Facts and Dimensions

### Introduction

**Facts** and **dimensions** are the most common types of tables in Caboodle. Other types of tables exist to
store additional information or facilitate joins. In this lesson, we will investigate some additional table types
and the role they play in Caboodles data model.

By the End of This Lesson, You Will Be Able To...
1. Define bridge tables
2. Explain the difference between a bridge table in the dbo schema and the database object of the
same name in the FullAccess schema
3. Define the **Entity Attribute Value  (EAV)** data structure
4. Identify **EAV tables** in Caboodle
5. Recognize the **EAV data structure** in other Caboodle tables
6. Understand the purpose of SetDim and DataMart tables


## Chapter 6  Beyond Facts and Dimensions


### Bridge tables

**Bridge tables** exist to capture many to many relationships, such as the one between patients and the
diagnoses on their problem list. In this particular case, DiagnosisBridge provides the connection. It
contains two columns DiagnosisComboKey (a surrogate key that represents a combination of diagnoses)
and DiagnosisKey (a lookup column to DiagnosisDim). By joining to DiagnosisBridge.DiagnosisComboKey
using PatientDim.ProblemComboKey, all the diagnoses on a patients problem list can be displayed. 


### General Structure

Every bridge table has two columns. They are called **<Name>ComboKey** and **<Name>Key**, where
<Name> is the name of the table to which a bridge has been formed. The <Name>Key column is a
lookup column to the corresponding dimension table. The **<Name>ComboKey** column is a **surrogate key**
that represents an observed unique combination of <Name>Key values.

A lookup column to a bridge table ends in ComboKey. A single bridge table can be referenced by multiple
Caboodle DMCs. Since bridge tables map a  to many  relationship, a join to a bridge table increases the
granularity of the results returned.

A single bridge table can be referenced multiple times by a single DMC, using multiple lookup columns.
For example, in HospitalAdmissionFact, the PresentOnAdmissionDiagnosisComboKey and
HospitalAcquiredDiagnosisComboKey columns join to DiagnosisBridge.


### Bridge Tables in FullAccess

In the FullAccess schema, bridge tables are combined with the dimension they link out to in a view that
has the same name as the bridge table. For example, FullAccess.DiagnosisBridge contains the name of the
diagnosis, even though the name is stored in dbo.DiagnosisDim.




## Beyond the Basics   EAV Data

For most tables in Caboodle, a row represents an entity (such as a department) and a column represents a
data point corresponding to that entity (such as the departments name). This is a convenient approach to
storing data where the collection of data points being tracked, sometimes referred to as the attributes,
doesnt change frequently. In cases where the attributes do often change, another data structure becomes
more appropriate. This data structure is known as the Entity Attribute Value (EAV) model.

SmartData Element data from Chronicles is an example of something that is extracted into an
entity attribute value format in Clarity and Caboodle. SmartData Element data in Chronicles
can be related to encounters, orders, episodes, and more. This data is stored in the HLV
master file in Chronicles and much of it gets extracted to AttributeValueDim tables in
Caboodle.




## Beyond the Basics   EAV Data

The three major components of the EAV data model are entities, attributes, and values. Lets define these
terms by looking at a particular example  suppose your organization is tracking patient hair color. In this
case, an entity is a patient, and the attribute is hair color. A value would be a particular patients hair color,
such as red.

## EAV Tables in Caboodle
In Caboodle, there are several forms of EAV data. The first and easiest to recognize are the DMCs that end
in the AttributeValueDim suffix. However, other DMCs, such as FlowsheetValueFact and
LabComponentResultFact also make use of the EAV model to store their data.

## AttributeValueDims
One form of EAV data in Caboodle is the AttributeValueDim DMCs. These tables contain attribute value
pairs and can be created for different entities. For instance, there is the PatientAttributeValueDim table to
go along with PatientDim, or the DepartmentAttributeValueDim table to go along with DepartmentDim.


## AttributeDim
The table that stores the list of all attributes used by the AttributeValueDim system in Caboodle is called
AttributeDim. It has one row per attribute and contains the name of the attribute (as well as some
additional metadata). 


 Excercise 5.2

USE Caboodle_Aug

SELECT MedicationOrderFact.MedicationOrderEpicId
		, DateDim.DisplayString Date
		, DepartmentDim.Name Department Name
		, PatientDim.PatientKey
		, MedicationDim.GenericName Medication Name
		, MedicationDim.MedicationEpicId
	FROM MedicationOrderFact
		INNER JOIN MedicationDim
			ON MedicationOrderFact.MedicationKey = MedicationDim.MedicationKey
		INNER JOIN DateDim
			ON MedicationOrderFact.OrderedDateKey = DateDim.DateKey
		INNER JOIN PatientDim
			ON MedicationOrderFact.PatientDurableKey = PatientDim.DurableKey 
			AND PatientDim.IsCurrent = 1
		INNER JOIN DepartmentDim
			ON MedicationOrderFact.DepartmentKey = DepartmentDim.DepartmentKey
	WHERE PatientDim._IsInferred = 1
			AND MedicationOrderFact.Count = 1



## Appendix   Appendix

### Appendix A Completing Your Training Track

### Appendix B End User Badge Guide

### Appendix C Additional Practice

### Appendix D Lesson 1   4 Review


## Strategy and Process for validating incoming data sources 

### 1. **Structural Integrity Check**
   - **Delimiter Consistency**: Verify that the data feed uses the same delimiter format (e.g., comma, tab).
   - **Column Count and Names**: Ensure the number of columns and column names are consistent with previous feeds.
   - **Data Type Consistency**: Validate that data types (e.g., string, integer, date) for each column match between this month's and prior months’ feeds.

### 2. **Provider Attribution and Affiliation Validation**
   - **Provider Validation**: Verify that each provider has a valid National Provider Identifier (NPI) and is listed on the current roster.
   - **Affiliation Check**: Confirm that providers are affiliated with an accepted practice or group in your network.
   
### 3. **Dual Enrollment Check**
   - **Multiple Insurer Enrollment**: Identify patients enrolled in more than one insurance payer or benefit type.
   - **Benefit Types & Plans**: Check patients enrolled in multiple benefit types (e.g., Medicare, Medicaid) or plan names and flag them for review.

### 4. **PCP Attribution Check**
   - Ensure that each patient is attributed to **only one** Primary Care Provider (PCP) and verify the PCP's validity based on the current roster.

### 5. **Reporting and Scoring**
   - Include a breakdown in the **scorecard** for:
     - Structural integrity results (e.g., pass/fail for each validation check).
     - Patient churn (new, lost, retained).
     - PCP attribution and affiliation verification.
     - Dual enrollment counts and details.
     - Anomaly flags for unusual structural or population changes.
   
This comprehensive approach ensures data integrity and meaningful population comparison, ensuring reliable, repeatable results for ongoing validation efforts.

## Strategy and Process for validating incoming data sources 

### 1. **Structural Integrity Check**
    **Delimiter Consistency** Verify that the data feed uses the same delimiter format (e.g., comma, tab).
    **Column Count and Names** Ensure the number of columns and column names are consistent with previous feeds.
    **Data Type Consistency** Validate that data types (e.g., string, integer, date) for each column match between this months and prior months feeds.

### 2. **Provider Attribution and Affiliation Validation**
    **Provider Validation** Verify that each provider has a valid National Provider Identifier (NPI) and is listed on the current roster.
    **Affiliation Check** Confirm that providers are affiliated with an accepted practice or group in your network.
   
### 3. **Dual Enrollment Check**
    **Multiple Insurer Enrollment** Identify patients enrolled in more than one insurance payer or benefit type.
    **Benefit Types & Plans** Check patients enrolled in multiple benefit types (e.g., Medicare, Medicaid) or plan names and flag them for review.

### 4. **PCP Attribution Check**
    Ensure that each patient is attributed to **only one** Primary Care Provider (PCP) and verify the PCPs validity based on the current roster.

### 5. **Reporting and Scoring**
    Include a breakdown in the **scorecard** for
      Structural integrity results (e.g., passfail for each validation check).
      Patient churn (new, lost, retained).
      PCP attribution and affiliation verification.
      Dual enrollment counts and details.
      Anomaly flags for unusual structural or population changes.
   
This comprehensive approach ensures data integrity and meaningful population comparison, ensuring reliable, repeatable results for ongoing validation efforts.

## Strategy and Process for validating incoming data sources 

### 1. **Structural Integrity Check**
    **Delimiter Consistency** Verify that the data feed uses the same delimiter format (e.g., comma, tab).
    **Column Count and Names** Ensure the number of columns and column names are consistent with previous feeds.
    **Data Type Consistency** Validate that data types (e.g., string, integer, date) for each column match between this months and prior months feeds.

### 2. **Provider Attribution and Affiliation Validation**
    **Provider Validation** Verify that each provider has a valid National Provider Identifier (NPI) and is listed on the current roster.
    **Affiliation Check** Confirm that providers are affiliated with an accepted practice or group in your network.
   
### 3. **Dual Enrollment Check**
    **Multiple Insurer Enrollment** Identify patients enrolled in more than one insurance payer or benefit type.
    **Benefit Types & Plans** Check patients enrolled in multiple benefit types (e.g., Medicare, Medicaid) or plan names and flag them for review.

### 4. **PCP Attribution Check**
    Ensure that each patient is attributed to **only one** Primary Care Provider (PCP) and verify the PCPs validity based on the current roster.

### 5. **Reporting and Scoring**
    Include a breakdown in the **scorecard** for
      Structural integrity results (e.g., passfail for each validation check).
      Patient churn (new, lost, retained).
      PCP attribution and affiliation verification.
      Dual enrollment counts and details.
      Anomaly flags for unusual structural or population changes.
   
This comprehensive approach ensures data integrity and meaningful population comparison, ensuring reliable, repeatable results for ongoing validation efforts.

![Solution](code.png)

    
![Solution](code.png)

    