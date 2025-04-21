from itertools import chain

COURSE_FOLDER = r"Chalmers/Courses/([A-Z]{3}\d{3}) ([^/]+)"


whitelist = list(
    chain(
        OBSIDIAN_FILES := [
            r"Chalmers/Media/.*",
            r"Chalmers/Anteckningar/.*",
            r"Chalmers/Excalidraw/.*",
            r"Chalmers/.trash/.*",
            r"Chalmers/.obsidian/.*",
        ],
        IGNORE := [
            r".*\.DS_Store$",
            r"Chalmers/.stignore",
            r"Chalmers/.*/\.git/.*",
            r"Chalmers/Tracker.xlsx",
            r"Chalmers(/.*)?/__pycache__/.*",
        ],
        SCHOOL_FILES := [
            COURSE_FOLDER + r"/Tentor/\1-\d{8}(-facit)?\.(pdf|docx)",
            COURSE_FOLDER + r"/Laboration( \d+)?/.*",
            COURSE_FOLDER + r"/Project( \d+)?/.*",
            COURSE_FOLDER + r"/Quiz( \d+)?/.*",
            COURSE_FOLDER + r"/Dugga( \d+)?/.*",
            COURSE_FOLDER + r"/Poster( \d+)?/.*",
            COURSE_FOLDER + r"/Seminarium( \d+)?/.*",
            COURSE_FOLDER + r"/Exercise( \d+)?/.*",
            COURSE_FOLDER + r"/Documents/.*",
            COURSE_FOLDER + r"/Inlämning( \d+)?/.*",
            r"Chalmers/Kurslitteratur/(\[SOLUTIONS\] )?[A-Za-z0-9 ]+\.(pdf|docx)",
        ],
    )
)
