# <div style="text-align:center">Software Requirements Specification (SRS) Document</div>

<br>

## 1. Introduction

### 1.1 Purpose

The purpose of this SRS document is to provide a comprehensive outline of the requirements for the development of the Brain Station 23 PLC Lunch Voting App. The application aims to address the challenge of providing different lunch options to employees by implementing a voting system for selecting daily menus.

### 1.2 Scope

The Lunch Voting App will allow employees to vote for their preferred restaurant menu, ensuring a fair and enjoyable process for deciding daily lunches. The application will include features such as authentication, restaurant creation, menu uploading, employee registration, voting, and result display.

<br>

## 2. Overall Description

### 2.1 Product Perspective

The Lunch Voting App will operate as an independent application within the Brain Station 23 PLC ecosystem. It will integrate with existing systems to facilitate employee participation in the menu selection process.

### 2.2 User Classes and Characteristics

**Employees:** Users who will interact with the application to vote for their preferred menu.

**Administrators:** Users responsible for managing restaurants, menus, and ensuring commitment to voting rules.

### 2.3 Operating Environment

The application will be accessible through web browsers, ensuring compatibility with various devices. It will utilize a SQL database for data storage and management.

<br>

## 3. Functional Requirements

### 3.1 Authentication

The system shall provide secure authentication for both employees and administrators.

### 3.2 Creating Restaurant

Administrators shall have the ability to create and manage restaurant profiles.

### 3.3 Uploading Menu for Restaurant

Administrators shall upload daily menus for their respective restaurants.

### 3.4 Menu Editing and Management

Administrators shall have the capability to edit and manage menus, including adding, updating, or removing dishes.

### 3.5 Creating Employee

Employees shall register profiles to participate in the voting process.

### 3.6 Getting Current Day Menu

Users shall have access to the current day's menus for voting.

### 3.7 Voting for Restaurant Menu

Employees shall be able to cast votes for their preferred restaurant menu.

### 3.8 Getting Results for the Current Day

The application shall display the winning restaurant menu for the day. A restaurant cannot win for three consecutive working days.

### 3.9 User Feedback

Employees should have the option to provide feedback on the quality of the selected menu for the day.

### 3.10 Historical Data and Reports

The system shall maintain historical data on past voting results, menus, and user preferences.

### 3.11 Logout

Users shall have the option to securely log out of their accounts.

<br>

## 4. Non-Functional Requirements

### 4.1 Performance

The system shall support a minimum of 1500 simultaneous users during voting times.

### 4.2 Security

User authentication data and voting information shall be encrypted using industry-standard protocols.

### 4.3 Maintainability

The codebase shall be well-documented, and the application architecture shall follow best practices to ensure ease of maintenance.

### 4.4 Scalability

The application shall be designed to scale horizontally and vertically to accommodate an increasing number of users and data.

### 4.5 Documentation

Comprehensive documentation, including a Project README.md and inline code comments, shall be maintained.

<br>

## 5. Constraints

### 5.1 Framework and Library

Any framework or library may be used for application development.

### 5.2 Database

The utilization of a SQL database is mandatory for data storage and retrieval.

### 5.3 Coding Standards

Adherence to PEP8 rules is mandatory.

### 5.4 Documentation

A Project README.md must be created, including launch instructions for the application.

### 5.5 Version Control

Proper version control using Git and GitHub is required for project management.
