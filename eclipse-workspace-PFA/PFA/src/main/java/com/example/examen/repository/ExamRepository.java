package com.example.examen.repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.example.examen.models.Exam;

@Repository
public interface ExamRepository extends CrudRepository<Exam, Long> {
    // Additional methods if needed
}