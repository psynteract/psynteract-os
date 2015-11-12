var gulp = require('gulp'),
  download = require('gulp-download'),
  zip = require('gulp-zip'),
  unzip = require('gulp-unzip');

gulp.task('download-dependencies', function() {
  // Download and copy python psynteract library
  download('https://github.com/psynteract/psynteract-py/archive/master.zip')
    .pipe(unzip())
    .pipe(gulp.dest('build/_dependencies/'));

  // Same for requests ...
  download('https://github.com/kennethreitz/requests/archive/v2.5.1.zip')
    .pipe(unzip())
    .pipe(gulp.dest('build/_dependencies/'));

  // ... and pycouchdb
  download('https://github.com/histrio/py-couchdb/archive/1.13.zip')
    .pipe(unzip())
    .pipe(gulp.dest('build/_dependencies/'));
})

gulp.task('bundle', function() {
  // Copy metadata
  gulp.src(['./README.md', './LICENSE', './NOTICE.md'])
    .pipe(gulp.dest('build/_output/'));

  // Copy extensions and plugins
  gulp.src(['./extensions/**/*'])
    .pipe(gulp.dest('build/_output/extensions/'));
  gulp.src(['./plugins/**/*'])
    .pipe(gulp.dest('build/_output/plugins/'));

  // Copy examples
  gulp.src(['./examples/**/*'])
    .pipe(gulp.dest('build/_output/examples/'));

  // Copy dependency files
  gulp.src('build/_dependencies/psynteract-py-master/psynteract/**/*')
    .pipe(gulp.dest('build/_output/extensions/psynteract_extension/psynteract'));
  gulp.src('build/_dependencies/requests-2.5.1/requests/**/*')
    .pipe(gulp.dest('build/_output/extensions/psynteract_extension/requests'));
  gulp.src('build/_dependencies/py-couchdb-1.13/pycouchdb/**/*')
    .pipe(gulp.dest('build/_output/extensions/psynteract_extension/pycouchdb'));

  // Copy backend
  // (this currently assumes that the backend
  // has been built manually)
  gulp.src('build/backend.json')
    .pipe(gulp.dest('build/_output/extensions/psynteract_extension/psynteract'));
});

gulp.task('zip', function() {
  // Zip up the _output directory
  gulp.src('build/_output/**/*')
    .pipe(zip('release.zip'))
    .pipe(gulp.dest('./'));
});

gulp.task('default', ['download-dependencies', 'bundle', 'zip']);
