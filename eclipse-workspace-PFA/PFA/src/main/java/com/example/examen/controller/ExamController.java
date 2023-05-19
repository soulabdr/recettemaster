package com.example.examen.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.examen.models.Exam;
import com.example.examen.repository.ExamRepository;

@RestController
@RequestMapping("/exams")
public class ExamController {

    private final ExamRepository examRepository;

    @Autowired
    public ExamController(ExamRepository examRepository) {
        this.examRepository = examRepository;
    }

    // Create Exam
    @PostMapping("/")
    public Exam createExam(@RequestBody Exam exam) {
        return examRepository.save(exam);
    }

    // Read Exam
    @GetMapping("/{id}")
    public Exam getExam(@PathVariable Long id) {
        return examRepository.findById(id).orElse(null);
    }

    // Update Exam
    @PutMapping("/{id}")
    public Exam updateExam(@PathVariable Long id, @RequestBody Exam updatedExam) {
        Exam exam = examRepository.findById(id).orElse(null);
        if (exam != null) {
            // Update the exam properties
            // ...
            return examRepository.save(exam);
        }
        return null;
    }

    // Delete Exam
    @DeleteMapping("/{id}")
    public void deleteExam(@PathVariable Long id) {
        examRepository.deleteById(id);
    }
   
}
