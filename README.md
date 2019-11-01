# Python Flask API Tutorial

Welcome to my Python Flask API tutorial! This tutorial was requested
by a viewer on my Twitch stream, and I thought it'd be a cool piece
of content, so here we are!

There's a few objectives I'd like to communicate with this tutorial
series beyond the surface objective of building an API with Python
and Flask.

* A basic understanding of architecture and software design
* Tradeoffs in software architecture
* Some fundamentals of development process and best practices

Accompanying this repository will be videos and blog posts for a more
linear experience as we build up this API. For each post/video I'll
have a branch in this repository as well, so you can follow along and
see the changes between each branch.

## The Project

In this tutorial, we'll be building a backend (with a minimal frontend) for a
restaurant reservation service. Partly inspired by my recent binging of Kitchen
Nightmares, it's also a decently complex, real-world project that has a lot of
room for creative improvements, is conceptually simple enough that everyone
kind of knows what it entails at a basic level, and it's got the basic
requirements of a full-stack application (database, permissions/authentication,
business logic) such that it makes an easy starting point if you wanted to make
one for real.

In a basic list, we want to satisfy these functional requirements:

* Multiple restaurants represented in the app
* A customer may make reservations at a restaurant for a date, time and number of people
* Each restaurant has a configuration of tables with seats
* A customer can search a time and get a list of restaurants with open seats
* A customer can also pick a restaurant and get their list of open times
* Customers can see their reservations list and modify/cancel them
* Restaurants can cancel reservations, but a reason is required

We might add more throughout the course of the tutorial, or I may expand the tutorial
in the future, but for now, that's a pretty solid, basic "version 1" of a restaurant
reservation application.

## The Concepts

This tutorial will be more heavily focused on the concepts, simply using Python and Vue(JS)
as a concrete method of implementing the concepts explained therein. If this becomes a video
series, it could very possibly end up with each segment being split into two videos, one for
concept and one for implementation.

_List of concepts coming soon!_

## The Stack

For simplicity's sake, we won't be using too many technologies.

* Python 3.4+ - might work on lower versions of py3, but I make no guarantees
* Python's Flask library - a minimal HTTP server library to give us full
architectural control
* PostgreSQL - no good reason _not_ to
* VueJS - it's a lightweight, component-based frontend framework with a very
low learning curve

The VueJS portion for this tutorial will be very minimal, mostly just there to
demonstrate how to connect a separated frontend and backend, and what some of
the pieces could look like in a frontend. You're free to skip the VueJS bits if
you're just interested in the backend parts.
