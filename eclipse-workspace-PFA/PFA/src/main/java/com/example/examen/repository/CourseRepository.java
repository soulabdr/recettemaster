package com.example.examen.repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.example.examen.models.Course;

@Repository
public interface CourseRepository extends CrudRepository<Course, Long> {
    // Additional methods if needed
}