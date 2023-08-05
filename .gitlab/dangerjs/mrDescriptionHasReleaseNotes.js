/**
 * Check if MR Description contains mandatory section "Release notes"
 *
 * Extracts the content of the "Release notes" section from the GitLab merge request description.
 *
 * @dangerjs WARN (if section missing, is empty or wrong markdown format)
 */
module.exports = function () {
    const mrDescription = danger.gitlab.mr.description;
    const wiki_link = `${process.env.DANGER_GITLAB_HOST}/espressif/esp-idf/-/wikis/rfc/How-to-write-release-notes-properly`;

    const regexSectionReleaseNotes = /## Release notes([\s\S]*?)(?=## |$)/;
    const regexValidEntry = /\s*[-*+]\s+.+/;
    const regexNoReleaseNotes = /no release note/i;

    const sectionReleaseNotes = mrDescription.match(regexSectionReleaseNotes);
    if (!sectionReleaseNotes) {
        warn('The `Release Notes` section seems to be missing. Please check if the section header in MR description is present and in the correct markdown format ("## Release Notes").\n\nSee <a href="${wiki_link}">Release Notes Format Rules</a>).');
        return null;
    }

    const lines = sectionReleaseNotes[1].split("\n").filter(s => s.trim().length > 0);
    let valid_entries_found = 0;
    let no_release_notes_found = false;
    let violations = [];

    lines.forEach((line) => {
        if (line.match(regexValidEntry)) {
            valid_entries_found++;
            const error_msg = check_entry(line);
            if (error_msg) {
                violations.push(error_msg);
            }
        } else if (line.match(regexNoReleaseNotes)) {
            no_release_notes_found = true;
        }
    });

    let error_output = ['']; // Add blank line on purpose, to avoid first line to be indented by dangerjs.
    if (violations.length > 0) {
        error_output = [...error_output, 'Invalid release note entries:', violations.join('\n')];
    }
    if (no_release_notes_found) {
        if (valid_entries_found > 0) {
            error_output.push('`No release notes` comment shows up when there is valid entry. Remove bullets before comments in release notes section.');
        }
    } else {
        if (!valid_entries_found) {
            error_output.push('The `Release Notes` section seems to have no valid entries. Add bullets before valid entries, or add `No release notes` comment to suppress this error if you mean to have no release notes.');
        }
    }

    if (error_output.length > 0) {
        //paragraphs joined by double `\n`s.
        error_output = [...error_output, `See <a href="${wiki_link}">Release Notes Format Guide</a>.`].join('\n\n');
        warn(error_output);
    }
    return null;
};

function check_entry(entry) {
    const entry_str = `- \`${entry}\``;
    const indent = "  ";

    if (entry.match(/no\s+release\s+note/i)) {
        return [entry_str, `${indent}- \`No release notes\` comment shouldn't start with bullet.`].join('\n');
    }

    const regex = /^(\s*)[-*+]\s+\[([^\]]+)\]\s+(.*)$/;
    const match = regex.exec(entry);
    if (!match) {
        return [entry_str, `${indent}- Please specify the [area] to which the change belongs (see guide). If this line is just a comment, remove the bullet.`].join('\n');
    }

    const area = match[2];
    const description = match[3].trim();
    let violations = [];

    if (match[1]) {
        violations.push(`${indent}- Release note entry should start from the beginning of line. (Nested release note not allowed.)`);
    }

    if (!/^[A-Z0-9]/.test(description)) {
        violations.push(`${indent}- Release note statement should start with a capital letter or digit.`);
    }

    if (violations.length > 0) {
        return [entry_str, ...violations].join('\n');
    }
    return null;
}
