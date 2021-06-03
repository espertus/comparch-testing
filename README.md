# Computer Architecture teaching/testing tools

## Mastery-based learning

This repository contains resources for *mastery-based learning* in 
undergraduate computer architecture courses. As principal Danielle
Salzberg has said: [[1]](https://www.kqed.org/mindshift/53241/how-mastery-based-learning-can-help-students-of-every-background-succeed)

> Mastery-based learning is a complete paradigm shift for most teachers. It means thinking about grading as a way to provide feedback, and not a random act that we do because the quarter is ending.

Principles of mastery-based learning include: [[2]](https://portal.ct.gov/SDE/Mastery-Based-Learning/10-Principles-of-Mastery-Based-Learning)

* Providing students with learning goals and the objective criteria for measuring them.

* Grading students based on these objective criteria and not on work habits, such as as neatness, timeliness, and effort.

* Giving students multiple opportunities to demonstrate mastery, ultimately grading them on *whether*, not *when*, they mastered the material.

These practices place a burden on teachers -- requiring them to create
and grade multiple versions of each test. This repository contains
scripts for generating questions and answers that can be uploaded to
Canvas or other learning management systems for automated testing.

## Organization

These directories contain code, sample output, and, in some cases, instructional material on the following topics:

* [caches](https://github.com/espertus/comparch-testing/tree/main/caches)
* [computer-arithmetic](https://github.com/espertus/comparch-testing/tree/main/computer-arithmetic)
* [instruction-encoding](https://github.com/espertus/comparch-testing/tree/main/instruction-encoding)

## Usage

Some of this information is specific to Canvas. I welcome pull requests for other LMSs.

### Setting up learning outcomes

The file [learning-outcomes.csv](https://github.com/espertus/comparch-testing/blob/main/learning-outcomes.csv) can be modified to meet your needs and [imported](https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-import-outcomes-for-a-course/ta-p/702) into the Outcomes section of your course. 

[Activiate](https://canvas.unl.edu/courses/50571/pages/step-1-activate-the-learning-mastery-gradebook-in-your-course) the Learning Mastery Gradebook.

### Generating questions

The code can be executed with Python 3 (tested with 3.9.0). Descriptions of each script appear in the appropriate subdirectory.

### Uploading questions

Generated files of questions and answers can be uploaded to Canvas through [Respondus 4.0](https://web.respondus.com/he/respondus/), which is unfortunately not free. I would be happy to learn of free alternatives. 

## Credits

This repository includes [qm.py](https://github.com/espertus/comparch-testing/blob/main/k-maps/qm.py) from [Thomas Pircher's implementation of the Quine McCluskey algorithm](https://github.com/tpircher/quine-mccluskey).

## About

This repository was created by Ellen Spertus based on material from her
Mills College course CS 111: Computer Architecture.
