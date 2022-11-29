import { 
    USER_PERMISSION, 
    SCIENCE_TUTOR, 
    SCIENCE_WORKER, 
    STUDENT_USER, 
    GRADUATE_USER 
} from "@/services/constants";


class ScienderUser {
    constructor(name, surname, patronymic, image, interests, about, status, speciality, work_links) {
        this.name = name;
        this.surname = surname;
        this.patronymic = patronymic;
        this.image = image;
        this.interests = interests;
        this.about = about;
        this.status = status;
        this.speciality = speciality;
        this.work_links = work_links;

        this.permission = USER_PERMISSION;
    }
}

class ScienderStudent extends ScienderUser {
    constructor(name, surname, patronymic, image, interests, about, status, speciality, work_links) {
        super(
            name, surname, patronymic, 
            image, interests, about, 
            status, speciality, work_links
        );
        this.permission = STUDENT_USER;
    }
}

class ScienderGraduateStudent extends ScienderUser {
    constructor(name, surname, patronymic, image, interests, about, status, speciality, work_links) {
        super(
            name, surname, patronymic, 
            image, interests, about, 
            status, speciality, work_links
        );
        this.permission = GRADUATE_USER;
    }
}


class ScienderScience extends ScienderUser {
    constructor(name, surname, patronymic, image, interests, about, status, speciality, work_links, job_title, academic_title, academic_degree, qualifying_links) {
        super(
            name, surname, patronymic, 
            image, interests, about, 
            status, speciality, work_links
        );

        this.job_title = job_title;
        this.academic_title = academic_title;
        this.academic_degree = academic_degree;
        this.qualifying_links = qualifying_links;
    }
}

class ScienderScienceTutor extends ScienderScience {
    constructor(name, surname, patronymic, image, interests, about, status, speciality, work_links, job_title, academic_title, academic_degree, qualifying_links) {
        super(
            name, surname, patronymic, 
            image, interests, about, 
            status, speciality, work_links, job_title, 
            academic_title, academic_degree, qualifying_links
        );
        this.permission = SCIENCE_TUTOR;
    }
}

class ScienderScienceWorker extends ScienderScience {
    constructor(name, surname, patronymic, image, interests, about, status, speciality, work_links, job_title, academic_title, academic_degree, qualifying_links) {
        super(
            name, surname, patronymic, 
            image, interests, about, 
            status, speciality, work_links, job_title, 
            academic_title, academic_degree, qualifying_links
        );
        this.permission = SCIENCE_WORKER;
    }
}


export {
    ScienderStudent,
    ScienderGraduateStudent,
    ScienderScienceTutor,
    ScienderScienceWorker,
};
