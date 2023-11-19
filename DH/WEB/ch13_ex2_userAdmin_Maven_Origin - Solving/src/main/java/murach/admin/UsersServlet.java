package murach.admin;

import java.io.*;
import java.util.*;
import javax.servlet.*;
import javax.servlet.http.*;

import murach.business.User1;
import murach.data.UserDB;

public class UsersServlet extends HttpServlet {

    @Override
    protected void doPost(HttpServletRequest request,
            HttpServletResponse response)
            throws ServletException, IOException {
        
        HttpSession session = request.getSession();

        String url = "/index.jsp";
        
        // get current action
        String action = request.getParameter("action");
        if (action == null) {
            action = "display_users";  // default action
        }
        
        // perform action and set URL to appropriate page
        if (action.equals("display_users")) {            
            // get list of users
            List<User1> displayUser = UserDB.selectUsers();
            
            // set list as a request attribute
            request.setAttribute("users", displayUser);
            // forward to index.jsp
            
            url = "/index.jsp";
        } 
        else if (action.equals("display_user")) {
            // get specified email
            String currentEmail = request.getParameter("email");
            
            // get user for email
            User1 currentUser = UserDB.selectUser(currentEmail);
            // set as session attribute
            session.setAttribute("user", currentUser);
            
           // request.setAttribute("user", currentUser);
            // forward to user.jsp
            url = "/user.jsp";
        }
        else if (action.equals("update_user")) {
            // get user from session
            User1 currentUser = (User1) session.getAttribute("user");
            // get new data from request
            String newFirstName = request.getParameter("firstName");
            String newLastName = request.getParameter("lastName");

            // update user
            currentUser.setFirstName(newFirstName);
            currentUser.setLastName(newLastName);
            
            // update user in database
            UserDB.update(currentUser);
            
            // get current list of users
            List<User1> displayUser = UserDB.selectUsers();
            // set as request attribute
            request.setAttribute("users", displayUser);
            // forward to index.jsp
            url = "/index.jsp";
        }
        else if (action.equals("delete_user")) {
            // get the user for the specified email
            String currentEmail = request.getParameter("email");
            
            User1 currentUser = UserDB.selectUser(currentEmail);

            // delete the user 
            UserDB.delete(currentUser);
            // get current list of users
            List<User1> userList = UserDB.selectUsers();
            // set as request attribute
            request.setAttribute("users",userList );
            // forward to index.jsp
            url = "/index.jsp";
        }
        
        getServletContext()
                .getRequestDispatcher(url)
                .forward(request, response);
    }    
    
    @Override
    protected void doGet(HttpServletRequest request,
            HttpServletResponse response)
            throws ServletException, IOException {
        doPost(request, response);
    }    
}